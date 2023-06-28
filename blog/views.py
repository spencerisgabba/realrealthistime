from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Post, Tag
from .serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostByTagAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        return Post.objects.filter(tags__id=tag_id)