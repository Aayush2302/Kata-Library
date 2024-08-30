from main.Book import Book
from main.User import User


class Library:
    def __init__(self):
        self.books_catalog = {}  # Dictionary to hold books

    def add_book(self, user: User, book: Book):
        if user.role not in ['Admin', 'Librarian']:
            raise ValueError('You do not have permission to add book')

        if book.identifier in self.books_catalog:
            raise ValueError("A Book with this identifier already exists ")
        self.books_catalog[book.identifier] = book

    # Remove Books [Admin,Librarian]
    def remove_book(self, user: User, identifier):
        if user.role not in ['Admin', 'Librarian']:
            raise ValueError('You do not have permission to remove book')

        if identifier not in self.books_catalog:
            raise ValueError("A Book with this identifier does not exist")

        del self.books_catalog[identifier]


if __name__ == "__main__":
    admin = User(username="admin_user", role="Admin")  #admin define with username & role
    librarian = User(username="librarian", role="Librarian")  #librarian define with username & role
    member = User(username="member_user", role="Member")  #member define with username & role
    library = Library()
    book1 = Book("001", "Death Note", "Light Yagami", "100", 2010, 5)

    # only admin & librarian can add the books
    library.add_book(admin, book1)

    # only admin & librarian can remove the books
    library.remove_book(admin,"001")
