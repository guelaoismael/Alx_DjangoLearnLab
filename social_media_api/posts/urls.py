from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import PostViewSet, CommentViewSet, feed_view

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename="post")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = [
  path("feed/", feed_view, name="feed"),
  path('', include(router.urls) )
]
