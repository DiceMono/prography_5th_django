from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)


@api_view(http_method_names=['GET'])
@permission_classes((IsAuthenticated,))
def like_or_dislike_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return Response(PostSerializer(post).data, status=status.HTTP_200_OK)
