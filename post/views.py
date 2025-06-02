from django.shortcuts import render
from .models import Post, Category, Comment
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
