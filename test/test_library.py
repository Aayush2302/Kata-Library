import unittest
from main.Library import Library
from main.Book import Book
from main.User import User


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.admin = User('admin_user', "Admin")
        self.librarian = User('librarian', "Librarian")
        self.member = User('member', "Member")
        self.new_user = User('Aayush', 'Member')

    # ADD BOOK

    # admin can add book
    def test_admin_add_book(self):
        book = Book("005", "Death Note", "Light Yagami", "300", 2010, 0)
        self.library.add_book(self.admin, book)
        self.assertIn("005", self.library.books_catalog)

    # member cannot add books
    def test_member_cannot_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        with self.assertRaises(PermissionError):
            self.library.add_book(self.member, book)

    # librarian can add books
    def test_librarian_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.librarian, book)
        self.assertIn("003", self.library.books_catalog)

    # REMOVE BOOK

    # admin can remove books
    def test_admin_can_remove_book(self):
        identifier = "003"
        # Ensure the book exists first
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        self.library.remove_book(self.admin, identifier)
        self.assertNotIn("003", self.library.books_catalog)

    # librarian can remove books
    def test_librarian_can_remove_book(self):
        identifier = "003"
        # Ensure the book exists first
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        self.library.remove_book(self.librarian, identifier)
        self.assertNotIn("003", self.library.books_catalog)

    # member can not remove books
    def test_member_cannot_remove_book(self):
        identifier = "003"
        # Ensure the book exists first
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        with self.assertRaises(PermissionError):
            self.library.remove_book(self.member, identifier)

    # BORROW_BOOK

    # only members can borrow the books

    def test_member_only_can_borrow_books(self):
        identifier = "005"
        book = Book("005", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        self.library.borrow_book(self.member, identifier)
        #check decreament
        self.assertEqual(self.library.books_catalog[identifier].stock, book.stock)

    # Admin cannot borrow the books
    def test_non_member_cannot_borrow_book(self):
        identifier = "003"
        with self.assertRaises(PermissionError):
            self.library.borrow_book(self.librarian, identifier)

    # Librarian can not borrow the books
    def test_borrowing_non_existent_book(self):
        identifier = "003"
        with self.assertRaises(ValueError):
            self.library.borrow_book(self.member, identifier)

    #RETURN BOOK

    # only members can do it
    def test_member_only_can_return(self):
        identifier = "005"
        book = Book("005", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        initial_stock = self.library.books_catalog[identifier].stock
        self.library.return_book(self.member, identifier)
        #check stock increament
        self.assertEqual(self.library.books_catalog[identifier].stock, initial_stock + 1)

    def test_non_member_cannot_return_book(self):
        identifier = "003"
        with self.assertRaises(PermissionError):
            self.library.return_book(self.librarian, identifier)

    def test_returning_non_existent_book(self):
        identifier = "999"
        with self.assertRaises(ValueError):
            self.library.return_book(self.member, identifier)

    def test_stock_increases_when_book_is_returned(self):
        identifier = "002"
        book = Book("002", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        initial_stock = self.library.books_catalog[identifier].stock
        self.library.return_book(self.member, identifier)
        self.assertEqual(self.library.books_catalog[identifier].stock, initial_stock + 1)

    #USER-TEST-SEction

    def test_only_admin_can_add_user(self):
        self.new_user = User("Aayush", "Member")
        try:
            self.library.add_user(self.member, self.new_user)
        except ValueError:
            self.fail("Admin should able to add user")

        # librarian cannot add User
        with self.assertRaises(ValueError) as context:
            self.library.add_user(self.librarian, self.new_user)
        self.assertEqual(str(context.exception), "Only admins have permission to add user")

        # member cannot add User
        with self.assertRaises(ValueError) as context:
            self.library.add_user(self.member, self.new_user)
        self.assertEqual(str(context.exception), "Only admins have permission to add user")

# REMOVE User
    def test_only_admin_can_remove_user_if_available(self):
        # self.new_user = User("Allen", "Member")
        # self.library.add_user(self.admin, self.new_user.username)
        if self.new_user.username in self.library.users_catalog:
            self.library.remove_user(self.admin, self.new_user.username)
            self.assertNotIn(self.new_user.username, self.library.users_catalog)
        else:
            self.fail("User is not in the catalog")



    def test_librarian_cannot_remove_user(self):
        # Ensure the librarian cannot remove a user
        with self.assertRaises(ValueError) as context:
            self.library.remove_user(self.librarian, self.new_user.username)
        self.assertEqual(str(context.exception), "Only admins have permission to remove users")

    def test_member_cannot_remove_user(self):
        # Ensure the member cannot remove a user
        with self.assertRaises(ValueError) as context:
            self.library.remove_user(self.member, self.new_user.username)
        self.assertEqual(str(context.exception), "Only admins have permission to remove users")


if __name__ == '__main__':
    unittest.main()
