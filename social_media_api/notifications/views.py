from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import permissions, generics, mixins
from rest_framework.decorators import api_view, permission_classes

class NotificationListView(mixins.RetrieveModelMixin, generics.GenericAPIView):
  
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    
    user = request.user
    notifications = Notification.objects.filter(actor=user).order_by('-timestamp')

    serializer = NotificationSerializer(notifications, many=True)

    return Response(serializer.data)