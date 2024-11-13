from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name

class Book(models.Model):
  class Meta:
     permissions = [
        ("can_add_book", "Can add book"),
        ("can_change_book", "Can change book"),
        ("can_delete_book", "Can delete book")
      ]
  title = models.CharField(max_length=120)
  author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name="books")

  def __str__(self):
    return f"{self.title} - {self.author}"

class Library(models.Model):
  name = models.CharField(max_length=120)
  books = models.ManyToManyField(Book)

  def __str__(self):
    return f"{self.name} - {self.books}"

class Librarian(models.Model):
  name = models.CharField(max_length=120)
  library = models.OneToOneField(Library, on_delete= models.CASCADE)
  
  def __str__(self):
    return f"{self.name} - {self.library}"


class UserProfile(models.Model):
  ROLE_CHOICES =[
    ('Admin', 'Admin'),
    ('Member', 'Member'),
    ('Librarian', 'Librarian'), 
  ]

  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  role = models.CharField(max_length=15, choices=ROLE_CHOICES)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()




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