from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, RegisterForm, UserProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Post, Comment
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
    template_name = "blog/listing_post.html"
    context_object_name = "posts"


class CreateView(generic.CreateView, LoginRequiredMixin):
    model = Post
    
    fields = ["title", "content"]
    template_name = "blog/creating_post.html"
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/viewing_post.html"

class UpdateView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    
    fields = ["title", "content"]
    template_name = "blog/updating_post.html"
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = "blog/deleting_post.html"
    success_url = reverse_lazy('posts')


# class AddCommentView(generic.View):
     
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         form = CommentForm()
#         return render(request, 'blog/comments/add_comment.html', {'form': form, 'post': post})

#     def post(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         form = CommentForm(request.POST)

#         if form.is_valid():
#             form.instance.author = request.user
#             form.instance.post = post
#             form.save()
#             return redirect('detail-post', pk=post.id)
#         return render(request, 'blog/comments/add_comment.html', {'form': form, 'post': post})


   

class CommentListView(generic.ListView):
    model = Comment
    template_name = "TEMPLATE_NAME"


class AddCommentView(generic.CreateView, LoginRequiredMixin):
   
   model = Comment
   fields = ['content']
   template_name="blog/comments/add_comment.html"

   def get_success_url(self):
      return reverse_lazy('detail-post', kwargs={'pk': self.kwargs['post_id']})
   
   def form_valid(self, form):
       form.instance.author = self.request.user  
       form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id']) 
       return super().form_valid(form)
   
class EditCommentView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin):
   
   model = Comment
   fields = ['content']
   template_name="blog/comments/edit_comment.html"

   def get_success_url(self):
      comment = self.get_object()
      return reverse_lazy('detail-post', kwargs={'pk': comment.post.pk})
   

class CommentDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = "blog/comments/delete_comment.html"
    
    def get_success_url(self):
      comment = self.get_object()
      return reverse_lazy('detail-post', kwargs={'pk': comment.post.pk})