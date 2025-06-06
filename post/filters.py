from django_filters import FilterSet, ModelChoiceFilter
from .models import Comment, Post


class CommentFilter(FilterSet):
    post = ModelChoiceFilter(queryset=Post.objects.all(), label='Объявление')
    class Meta:
        model = Comment
        fields = ['post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = kwargs.get('request')
        if request and hasattr(request, 'user'):
            self.filters['post'].queryset = Post.objects.filter(author=request.user)