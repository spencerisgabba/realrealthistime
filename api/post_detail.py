from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def serverless_function(request, pk):
        view = PostDetailAPIView.as_view()
        response = view(request, pk=pk)
        return response