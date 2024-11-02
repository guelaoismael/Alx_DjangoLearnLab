# create.md

# Command to create a Book instance with title "1984", author "George Orwell", and publication year 1949.

from bookshelf.models import Book
book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
book.save()
book

# Expected output

# <Book: Book object (1)>

from bookshelf.models import Book
Book.objects.get(title="1984")

# <Book: title : 1984, author : George Orwell, publication year : 1949>

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"

# 'Nineteen Eghty-Four'

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# (1, {'bookshelf.Book': 1})

# <QuerySet []>
