from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import  reverse_lazy

from .models import Library
from .models import Book

# Create your views here.

def list_books(request):
  
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.all()
    

class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('relationship_app:login')
    template_name = 'relationship_app/register.html'

    def form_valid(self, form):
        # Save the new user, then log them in
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
