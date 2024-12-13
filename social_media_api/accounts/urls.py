from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, profile_view, FollowUser, UnfollowUser


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('profile/', profile_view, name='logout'),
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow-user'),
]