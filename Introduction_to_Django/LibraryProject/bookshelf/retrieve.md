from bookshelf.models import Book
Book.objects.get(title="1984")

# <QuerySet [<Book: title : 1984, author : George Orwell, publication year : 1949>]>
