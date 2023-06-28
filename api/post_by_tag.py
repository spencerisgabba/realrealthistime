from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer

class PostByTagAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        return Post.objects.filter(tags__id=tag_id)

    def serverless_function(request, tag_id):
        view = PostByTagAPIView.as_view()
        response = view(request, tag_id=tag_id)
        return response