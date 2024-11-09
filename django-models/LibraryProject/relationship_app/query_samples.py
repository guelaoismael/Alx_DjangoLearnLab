from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
   
        books_by_author = Book.objects.filter(author = author_name)
        return books_by_author

def get_books_in_library(library_name):
    
        library = Library.objects.get(name=library_name)
        return library.books.all()
   

def get_librarian_for_library(library_name):
        library = Library.objects.get(name=library_name)
        return library.librarian