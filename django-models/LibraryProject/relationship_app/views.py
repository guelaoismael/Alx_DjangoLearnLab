from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

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

# Check role function
def check_role(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator

# Vue Admin
@user_passes_test(check_role('Admin'), login_url='/login/')
def Admin(request):
    return render(request, 'relationship_app/admin_view.html')

# Vue Bibliothécaire
@user_passes_test(check_role('Librarian'), login_url='/login/')
def Librarian(request):
    return render(request, 'relationship_app/librarian_view.html')

# Vue Membre
@user_passes_test(check_role('Member'), login_url='/login/')
def Member(request):
    return render(request, 'relationship_app/member_view.html')