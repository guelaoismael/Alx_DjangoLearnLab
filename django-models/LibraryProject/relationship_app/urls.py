from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import RegistrationView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = 'relationship_app'
urlpatterns = [
  path("books/", list_books, name='books'),
  path("libraries/", LibraryDetailView.as_view(), name='libraries'),
  path("register/", RegistrationView.as_view(), name="register"),
  path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
  path("logout/", LogoutView.as_view(), name='logout')

]