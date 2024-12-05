from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .views import PostByTagListView, register_view,CommentDeleteView,CommentUpdateView, CommentCreateView, profile_view, CreateView, DeleteView, UpdateView, ListView, DetailView, search_posts

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
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<str:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
