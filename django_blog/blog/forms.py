from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag
from taggit.forms import TagWidget


class RegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)
  
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["username", "email"]

class PostForm(forms.ModelForm):

  # tags = forms.CharField(max_length=100, required=False)

  def save(self, commit=True):
    post = super().save(commit=False)

    if commit:
      post.save()
    tag_names = self.cleaned_data_get('tags', '')
    if tag_names:
      tag_names = [name.strip() for name in tag_names.split(',')]
      for name in tag_names:
          tag, created = Tag.objects.get_or_create(name=name)
          post.tags.add(tag)
    return post
  class Meta:
    model = Post
    fields = ["title", "content","tags"]
    widgets = {
            "tags": TagWidget(),
        }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]