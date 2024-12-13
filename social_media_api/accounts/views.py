from django.shortcuts import render
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegistrationSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()
# Create your views here.
@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token'] = token      
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET',])   
def profile_view(request):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, pk):
    # User = settings.AUTH_USER_MODEL  
    if request.method != "POST":
        return Response({"error": "This endpoint only supports POST requests."}, status=405)
    
    
    if request.method == 'POST':

        try:
            user_to_follow = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "The user that you want to follow doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        request.user.following.add(user_to_follow)
        
        return Response({"succes": "You follow now the user"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, pk):
    # User = settings.AUTH_USER_MODEL  
    if request.method != "POST":
        return Response({"error": "This endpoint only supports POST requests."}, status=405)
    
    
    if request.method == 'POST':

        try:
            user_to_unfollow = User.objects.get(pk=pk)
            
        except User.DoesNotExist:
            return Response({"error": "The user that you want to unfollow doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        if user_to_unfollow not in request.user.following.all():
            return Response({"error": "This user doesn't exist in your following list"}, status=status.HTTP_200_OK)
    
        request.user.following.remove(user_to_unfollow)
        
        return Response({"succes": "You unfollow the user"}, status=status.HTTP_200_OK)
