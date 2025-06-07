from django_filters import FilterSet, ModelChoiceFilter
from .models import Comment, Post


class CommentFilter(FilterSet):
    post = ModelChoiceFilter(
        queryset=Post.objects.none(),
        label='Объявление'
    )

    class Meta:
        model = Comment
        fields = ['post']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if request and request.user.is_authenticated:
            self.filters['post'].queryset = Post.objects.filter(author=request.user)