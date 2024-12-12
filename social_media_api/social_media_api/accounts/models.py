from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

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
   
   bio = models.TextField()
   profile_picture = models.ImageField(null=True, blank=True)
   followers = models.ManyToManyField("self", symmetrical=False)

   objects = CustomUserManager()