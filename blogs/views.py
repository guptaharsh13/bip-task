from rest_framework.viewsets import ModelViewSet
from .models import Post, Tag, Comment
from .serializers import PostSerializer, TagSerializer, CommentSerializer
from .pagination import CustomPagination
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filterset_fields = ("title", "tags__name", "comments__title",
                        "author__first_name", "author__last_name", "author__username", "likes__first_name", "likes__last_name", "likes__username", "published_on", "updated")

    search_fields = ("title", "body", "tags__name", "comments__title", "comments__body",
                     "author__first_name", "author__last_name", "author__username", "likes__first_name", "likes__last_name", "likes__username")

    ordering_fields = ("title", "published_on", "updated")
    pagination_class = CustomPagination
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "burst"


class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    filterset_fields = ("name", "added_on", "updated")
    search_fields = ("name")
    ordering_fields = ("name", "added_on", "updated")
    pagination_class = CustomPagination
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "burst"


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filterset_fields = ("title", "body", "author__first_name", "author__last_name", "author__username",
                        "likes__first_name", "likes__last_name", "likes__username", "posted_on", "updated")

    search_fields = ("title", "body", "author__first_name", "author__last_name",
                     "author__username", "likes__first_name", "likes__last_name", "likes__username")

    ordering_fields = ("title", "posted_on", "updated")
    pagination_class = CustomPagination
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "burst"
