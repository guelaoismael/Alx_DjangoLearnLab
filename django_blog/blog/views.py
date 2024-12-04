from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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



class ListView(generic.ListView):
    model = Post
    template_name = "blog/list_post.html"
    context_object_name = "posts"


class CreateView(generic.CreateView, LoginRequiredMixin):
    model = Post
    
    fields = ["title", "content"]
    template_name = "blog/new_post.html"
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail_post.html"

class UpdateView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    
    fields = ["title", "content"]
    template_name = "blog/update_post.html"
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('posts')


