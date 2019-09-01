from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'created_at', 'updated_at',)

    def create(self, validated_data):
        view_context = self.context.get("view")
        validated_data["author"] = view_context.request.user
        validated_data["post_id"] = view_context.kwargs.get("pk")
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'image', 'title', 'body', 'created_at', 'updated_at', 'comments', 'likes')

    def create(self, validated_data):
        view_context = self.context.get("view")
        validated_data["author"] = view_context.request.user
        return super().create(validated_data)
