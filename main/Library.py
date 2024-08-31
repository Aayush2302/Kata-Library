from main.Book import Book
from main.User import User


class Library:
    def __init__(self):
        self.books_catalog = {}  # Dictionary to hold books
        self.users_catalog = {}  # Dictionary to hold Users

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

    def borrow_book(self, user: User, identifier):
        if user.role != 'Member':
            raise ValueError('Only members have permission to borrow a book')

        if identifier not in self.books_catalog:
            raise ValueError("Book not found in the catalog")

        book = self.books_catalog[identifier]
        if book.stock <= 0:
            raise ValueError("Book is not available")

        book.update_stock(-1)

    #Retrun_book only Member can do this
    def return_book(self, user: User, identifier):
        if user.role != 'Member':
            raise PermissionError('Only members have permission to return book')

        if identifier not in self.books_catalog:
            raise ValueError("Book not found in the catalog")

        book = self.books_catalog[identifier]
        book.update_stock(1)

    # showing all available books
    def view_available_books(self):
        for book in self.books_catalog.values():
            if book.is_available():
                print(f"Identifier: {book.identifier}, Title:{book.title}, Author:{book.author}, Stock:{book.stock}")

    # USER-SECTION

    #add User

    def add_user(self, admin_user: User, user: User):
        #admin_user must be the Admin
        if admin_user.role != 'Admin':
            raise ValueError('Only admins have permission to add user')
        # user already exist
        if user.username in self.users_catalog:
            raise ValueError("A User with this username already exists ")
        # else user added
        self.users_catalog[user.username] = user

    def remove_user(self, admin_user: User, user: User):
        if admin_user.role != 'Admin':
            raise PermissionError('Only admins have permission to remove user')

        if user.username not in self.users_catalog:
            raise ValueError("A User with this username does not exist")

        del self.users_catalog[user.username]

    # USER LIST
    def user_list(self):
        for user in self.users_catalog.values():
            print(f"Username: {user.username},Role: {user.role}")


if __name__ == "__main__":
    # admin define with username & role
    admin = User(username="admin_user", role="Admin")
    # librarian define with username & role
    librarian = User(username="librarian", role="Librarian")
    # member define with username & role
    member = User(username="member_user", role="Member")
    library = Library()

    # TESTING PURPOSE
    print("Book Added")
    book1 = Book("001", "Death Note", "Light Yagami", "100", 2010, 3)
    book2 = Book("002", "Super-man", "DC", "200", 2000, 2)
    book3 = Book("003", "Spider-man", "Marvel-Comics", "300", 2004, 1)

    library.add_book(admin, book1)
    library.add_book(librarian, book2)
    library.add_book(admin, book3)

    library.view_available_books()

    member1 = User("Alex", "Member")
    member2 = User("Allen", "Member")
    member3 = User("Bob", "Member")
    print("User Added")
    library.add_user(admin, member1)
    library.add_user(admin, member2)
    library.add_user(admin, member3)

    library.user_list()
    print("Book Borrowed")
    library.borrow_book(member1, "002")
    library.borrow_book(member2, "003")

    library.view_available_books()

    print("Book returned")
    library.return_book(member1, "002")
    library.return_book(member2, "003")

    library.view_available_books()

