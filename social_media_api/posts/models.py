from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
  title = models.TextField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.author.username} - {self.post.title}"

class Like(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username} liked {self.post.title}"