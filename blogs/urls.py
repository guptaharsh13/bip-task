from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import PostView, TagView, CommentView

router = DefaultRouter()
router.register("posts", viewset=PostView, basename="posts")
router.register("tags", viewset=TagView, basename="tags")
router.register("comments", viewset=CommentView, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
]
