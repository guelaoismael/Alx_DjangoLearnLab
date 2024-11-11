from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=120)

  def __str__(self):
    return f"{self.name}"

class Book(models.Model):
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
