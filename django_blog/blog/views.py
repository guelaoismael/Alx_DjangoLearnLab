from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegistrationView(CreateView):
  
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "blog/signup.html"


@login_required
def profile_view(request):
    # This view can only be accessed by authenticated users
    return render(request, 'blog/profile.html')