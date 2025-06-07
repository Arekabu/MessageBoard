from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import VerificationCode
from .forms import CustomRegisterForm
from post.models import Comment
from post.filters import CommentFilter



class CustomRegisterView(CreateView):
    model = User
    form_class = CustomRegisterForm
    template_name = 'signup_page.html'
    success_url = ''

    def form_valid(self, form):
        pass



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
        context['filterset'] = CommentFilter(self.request.GET, comments)

        return context

