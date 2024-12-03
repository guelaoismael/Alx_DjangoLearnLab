from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import register_view, profile_view

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path('', profile_view, name='home'),
    path('posts/',profile_view, name='posts'),
]
