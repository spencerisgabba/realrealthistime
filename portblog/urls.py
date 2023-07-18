from django.urls import path
from blog.views import PostListAPIView, PostDetailAPIView, PostByTagAPIView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/tag/<int:tag_id>/', PostByTagAPIView.as_view(), name='posts-by-tag-api'),
]