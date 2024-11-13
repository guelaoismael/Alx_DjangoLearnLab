from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()

  def __str__(self):
    return f"title : {self.title}, author : {self.author}, publication year : {self.publication_year}"


class CustomUserManager(BaseUserManager):
   
   def create_user(self, username, email, password=None, **extra_fields):
      
      email = self.normalize_email(email)
      user = self.model(username=username, email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)

      return user
   

   def create_superuser(self, username, email, password=None, **extra_fields):
      
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)

      return self.create_user(username, email, password, **extra_fields)
   

# Set up the custom user model

class CustomUser(AbstractUser):
   
   date_of_birth = models.DateField()
   profile_photo = models.ImageField()

   objects = CustomUserManager()