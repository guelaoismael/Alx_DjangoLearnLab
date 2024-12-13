from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, profile_view, follow_user, unfollow_user


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('profile/', profile_view, name='logout'),
    path('follow/<int:pk>/', follow_user, name='follow-user'),
    path('unfollow/<int:pk>/', unfollow_user, name='unfollow-user'),
]