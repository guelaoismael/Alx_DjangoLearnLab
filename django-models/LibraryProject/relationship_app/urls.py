from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = 'relationship_app'
urlpatterns = [
  path("books/", list_books, name='books'),
  path("libraries/", LibraryDetailView.as_view(), name='libraries'),
  path("register/", views.register.as_view(template_name="relationship_app/register.html"), name="register"),
  path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
  path("logout/", LogoutView.as_view(), name='logout')

]