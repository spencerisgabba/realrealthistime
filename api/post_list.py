from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def serverless_function(request):
        view = PostListAPIView.as_view()
        response = view(request)
        return response