from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, generics, mixins
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from django.shortcuts import render
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
  
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ["title", "content"]


class CommentViewSet(viewsets.ModelViewSet):
  
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed_view(request):
    user = request.user
    following_users = user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
 

class LikePostView(mixins.CreateModelMixin, generics.GenericAPIView):
   
   queryset = Post.objects.all()
   serializer_class = PostSerializer
   permission_classes = [permissions.IsAuthenticated]

   def post(self, request, *args, **kwargs):
      try:
        post = Post.objects.get(pk = self.kwargs['pk'])
      except Post.DoesNotExist:
         return Response({"error": "This post doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
      
      user = request.user

      if Like.objects.filter(post=post, user=user).exists():
        return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
      
      Like.objects.create(user=user, post=post)

      if post.author != user:
        Notification.objects.create(
          recipient=post.author,
          actor=user,
          verb="liked your post",
          target=post
        )

      return Response({"success": "Post liked successfully."}, status=status.HTTP_201_CREATED)
   

class UnlikePostView(mixins.CreateModelMixin, generics.GenericAPIView):
   
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request, *args, **kwargs):
    try:
      post = Post.objects.get(pk = self.kwargs['pk'])
    except Post.DoesNotExist:
        return Response({"error": "This post doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
      
    user = request.user

    if not Like.objects.filter(post=post, user=user).first():
        return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
    Like.objects.filter(post=post, user=user).first().delete()  
    
    return Response({"success": "Post unliked successfully."}, status=status.HTTP_200_OK)