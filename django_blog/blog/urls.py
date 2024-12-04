from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .views import register_view, profile_view, CreateView, DeleteView, UpdateView, ListView, DetailView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("", profile_view, name="home"),
    path('posts/', ListView.as_view(), name='posts'),
    path('posts/new/', CreateView.as_view(), name='new-post'),
    path('posts/<int:pk>/edit/', UpdateView.as_view(), name='update-post'),
    path('posts/<int:pk>/',DetailView.as_view(), name='detail-post'),
    path('posts/<int:pk>/delete/',DeleteView.as_view(), name='delete-post'),
    
]
