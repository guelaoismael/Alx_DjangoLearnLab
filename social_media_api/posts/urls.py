from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import PostViewSet, CommentViewSet, feed_view, LikePostView, UnlikePostView

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename="post")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = [
  path("feed/", feed_view, name="feed"),
  path("posts/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
  path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
  path('', include(router.urls) )
]
