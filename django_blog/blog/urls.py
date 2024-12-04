from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .views import register_view,CommentDeleteView,EditCommentView, AddCommentView, profile_view, CreateView, DeleteView, UpdateView, ListView, DetailView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("", profile_view, name="home"),
    path('post/', ListView.as_view(), name='posts'),
    path('post/new/', CreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/',DetailView.as_view(), name='detail-post'),
    path('post/<int:pk>/delete/',DeleteView.as_view(), name='delete-post'),
    path('posts/<int:post_id>/comments/new/', AddCommentView.as_view(), name='add-comment'),
    path('comments/<int:pk>/edit/', EditCommentView.as_view(), name='edit-comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]
