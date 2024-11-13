# create.md

# Command to create a Book instance with title "1984", author "George Orwell", and publication year 1949.

from bookshelf.models import Book
book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
book.save()
book

# Expected output

# <Book: Book object (1)>
