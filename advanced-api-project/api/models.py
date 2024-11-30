from django.db import models

# Create your models here.
#This model represent the author
class Author(models.Model):
  name = models.CharField(max_length=100)

#This model represent a Book, Each book is linked to one author
class Book(models.Model):
  title = models.CharField(max_length=100)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')