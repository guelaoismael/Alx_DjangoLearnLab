from django.urls import path
from . import views

app_name = 'relationship_app'
urlpatterns = [
  path("/books", views.list_books, name='books'),
  path("/libraries", views.LibraryDetailsView.as_view(), name='libraries')
]