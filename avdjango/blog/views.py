from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serialized_data = PostSerializer(instance=posts, many=True).data
        return Response(serialized_data)


class CreatePostView(APIView):

    def post(self, request):
        post_data = request.data
        title = post_data['title']
        description = post_data['description']

        post = Post(title=title, description=description)

        try:
            post.save()
        except Exception as e:
            return Response({
                'message': 'Post was not saved successfully'
            })

        return Response({
            'message': "Post Saved Successfully"
        })
