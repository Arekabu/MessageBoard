from django.urls import path
from .views import PostDetail, PostCreate, PostUpdate, PostList


urlpatterns = [
    path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
    path('create', PostCreate.as_view(), name = 'post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('', PostList.as_view(), name = 'post_list'),
]