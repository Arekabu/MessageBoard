from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=19, unique=True)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = RichTextUploadingField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        path = reverse('post_detail', args=[str(self.id)])
        return path

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})

