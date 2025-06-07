import string
import random
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, FormView
from .forms import CustomRegisterForm, VerificationForm
from .models import VerificationCode
from post.models import Comment
from post.filters import CommentFilter
from .tasks import send_verification_code


class CustomRegisterView(CreateView):
    model = User
    form_class = CustomRegisterForm
    template_name = 'signup_page.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        code = ''.join(random.choices(string.ascii_lowercase+string.digits, k=6))
        email = user.email

        VerificationCode.objects.create(user=user, code=code)

        send_verification_code(email, code)
        self.request.session['verify_user_pk'] = user.pk

        return redirect('verify_page')


class VerifyCode(FormView):
    template_name = 'verify_page.html'
    form_class = VerificationForm
    success_url = settings.SITE_URL

    def form_valid(self, form):
        code = form.cleaned_data['code']
        user_pk = self.request.session.get('verify_user_pk')
        print(code)
        print(user_pk)

        verification_code = VerificationCode.objects.filter(
            user__pk=user_pk,
            code=code
        ).first()

        if verification_code:
            user = User.objects.get(pk=user_pk)
            user.is_active = True
            user.save()

            login(self.request, user)

            verification_code.delete()

            del self.request.session['verify_user_pk']
            return redirect(self.get_success_url())
        else:
            form.add_error('code', 'Неверный код подтверждения')
            return self.form_invalid(form)


class UserPage(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'user_page.html'
    context_object_name = 'user'

    def test_func(self):
        user = self.get_object()

        return user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        comments = Comment.objects.filter(post__author=user)

        context['filterset'] = CommentFilter(
            self.request.GET,
            queryset=comments,
            request=self.request
        )
        return context

