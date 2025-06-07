from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from .filters import CommentFilter


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        comments = Comment.objects.filter(post=post, approved=True)
        context['comments'] = comments

        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

    def test_func(self):
        post = self.get_object()

        return post.author == self.request.user

class PostDelete(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()

        return post.author == self.request.user

class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    paginate_orphans = 2

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user

        return super().form_valid(form)

class BulkApproveCommentsView(View):
    def post(self, request):
        comment_ids = request.POST.getlist('comment_ids')
        action = request.POST.get('action')

        if not comment_ids:
            messages.error(request, "Выберите хотя бы один комментарий!")

            return redirect('user_page', pk=request.user.pk)

        comments = Comment.objects.filter(id__in=comment_ids)

        if action == 'approve':
            comments.update(approved=True)
            messages.success(request, f"Одобрено {len(comments)} комментариев")
        elif action == 'delete':
            deleted_count = comments.count()
            comments.delete()
            messages.success(request, f"Удалено {deleted_count} комментариев")

        return redirect('user_page', pk=request.user.pk)

