from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serialized_data = PostSerializer(instance=posts, many=True).data
        return Response(serialized_data)

