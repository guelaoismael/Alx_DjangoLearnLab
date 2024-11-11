from django.urls import path
from .views import list_books
from .views import LibraryDetailView

app_name = 'relationship_app'
urlpatterns = [
  path("/books", list_books, name='books'),
  path("/libraries", LibraryDetailView.as_view(), name='libraries')
]