from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'author',
           'category',
       ]
       widgets = {
           'category': forms.CheckboxSelectMultiple,
       }
       labels = {
           'title': 'Заголовок:',
           'text': 'Текст:',
           'author': 'Автор:',
           'category': 'Категория:',
       }
