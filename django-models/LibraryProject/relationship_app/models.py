from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=120)

class Book(models.Model):
  title = models.CharField(max_length=120)
  author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name="books")

class Library(models.Model):
  name = models.CharField(max_length=120)
  books = models.ManyToManyField(Book)

class Librarian(models.Model):
  name = models.CharField(max_length=120)
  library = models.OneToOneField(Library)
