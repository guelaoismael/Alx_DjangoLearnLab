from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegisterForm()
  return render(request, 'blog/register.html', {'form':form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})