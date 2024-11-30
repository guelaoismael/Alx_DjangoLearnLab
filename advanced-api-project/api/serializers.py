from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Here is a BookSerializer with a custom validation that ensure that the publication_year is not in the future
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book  
    fields = '__all__'

    def validate(self, data):
      if data['publication_year'] > datetime.now().year:
        raise serializers.ValidationError("publication_year can not be in the future")
      return data

# Serializes the Author model. Includes a nested serializer for books related to the author.
class AuthorSerializer(serializers.ModelSerializer):
  
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = ['id', 'name', 'books']