from rest_framework import serializers
from .models import Notification
from posts.serializers import PostSerializer
from posts.models import Post


class NotificationSerializer(serializers.ModelSerializer):

  target = serializers.SerializerMethodField()
  
  class Meta:
    model = Notification
    fields = ['id', 'actor', 'verb', 'timestamp', 'target']

  def get_target(self, obj):
    if isinstance(obj.target, Post):
        return PostSerializer(obj.target).data
    return str(obj.target)