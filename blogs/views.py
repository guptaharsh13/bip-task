from rest_framework.viewsets import ModelViewSet
from .models import Post, Tag, Comment
from .serializers import PostSerializer, TagSerializer, CommentSerializer

# Create your views here.


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
