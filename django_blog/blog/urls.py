from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView, profile_view


urlpatterns = [
  path("login/", view=LoginView.as_view(template_name="blog/login.html"), name="login"),
  path("logout/", view=LogoutView.as_view(), name="logout"),
  path("register/", view=RegistrationView.as_view(), name="register"),
  path("profile/", view=profile_view, name="profile"),
]