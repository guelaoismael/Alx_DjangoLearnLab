from django.shortcuts import render
from django.views import generic

from .models import Library
from .models import Book

# Create your views here.

def list_books(request):
  
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})

class LibraryDetailsView(generic.ListView):
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.all()