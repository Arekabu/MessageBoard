from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'category',
       ]
       widgets = {
           'category': forms.RadioSelect,
       }
       labels = {
           'title': 'Заголовок:',
           'text': 'Текст:',
           'category': 'Категория:',
       }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
