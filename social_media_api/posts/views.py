from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

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
 
