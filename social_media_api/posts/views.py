from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from django.shortcuts import render
from .models import Post, Comment
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
 
