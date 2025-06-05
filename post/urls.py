from django.urls import path
from .views import PostDetail, PostCreate, PostUpdate, PostList, CommentCreate, PostDelete


urlpatterns = [
    path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
    path('create/', PostCreate.as_view(), name = 'post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_create'),
    path('', PostList.as_view(), name = 'post_list'),
    path('posts/', PostList.as_view(), name = 'post_list'),
]