import unittest
from main.Library import Library
from main.Book import Book
from main.User import User

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.admin = User('admin_user', "Admin")
        self.librarian = User('librarian_user', "Librarian")
        self.member = User('member_user', "Member")
        self.new_user = User('Aayush', 'Member')

    # ADD BOOK

    def test_admin_add_book(self):
        book = Book("005", "Death Note", "Light Yagami", "300", 2010, 0)
        self.library.add_book(self.admin, book)
        self.assertIn("005", self.library.books_catalog)

    def test_member_cannot_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        with self.assertRaises(PermissionError):
            self.library.add_book(self.member, book)

    def test_librarian_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.librarian, book)
        self.assertIn("003", self.library.books_catalog)

    # REMOVE BOOK

    def test_admin_can_remove_book(self):
        identifier = "003"
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        self.library.remove_book(self.admin, identifier)
        self.assertNotIn("003", self.library.books_catalog)

    def test_librarian_can_remove_book(self):
        identifier = "003"
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        self.library.remove_book(self.librarian, identifier)
        self.assertNotIn("003", self.library.books_catalog)

    def test_member_cannot_remove_book(self):
        identifier = "003"
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        with self.assertRaises(PermissionError):
            self.library.remove_book(self.member, identifier)

    # BORROW BOOK

    def test_member_only_can_borrow_books(self):
        identifier = "005"
        book = Book(identifier, "Death Note", "Light Yagami", "300", 2010, 4)  # Set initial stock to 4
        self.library.add_book(self.admin, book)

        # Borrow the book
        self.library.borrow_book(self.member, identifier)

        # Check that the stock decreased by 1
        self.assertEqual(self.library.books_catalog[identifier].stock, 3)  # 4 - 1 = 3

    def test_non_member_cannot_borrow_book(self):
        identifier = "003"
        with self.assertRaises(PermissionError):
            self.library.borrow_book(self.librarian, identifier)

    def test_borrowing_non_existent_book(self):
        identifier = "003"
        with self.assertRaises(ValueError):
            self.library.borrow_book(self.member, identifier)

    # RETURN BOOK

    def test_member_only_can_return(self):
        identifier = "005"
        book = Book("005", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin, book)
        self.library.borrow_book(self.member, identifier)  # First borrow the book to test return
        initial_stock = self.library.books_catalog[identifier].stock
        self.library.return_book(self.member, identifier)
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
        self.library.borrow_book(self.member, identifier)  # First borrow the book to test return
        initial_stock = self.library.books_catalog[identifier].stock
        self.library.return_book(self.member, identifier)
        self.assertEqual(self.library.books_catalog[identifier].stock, initial_stock + 1)

    # USER TEST SECTION

    def test_only_admin_can_add_user(self):
        try:
            self.library.add_user(self.admin, self.new_user)
        except PermissionError:
            self.fail("Admin should be able to add a user")

        with self.assertRaises(PermissionError):
            self.library.add_user(self.librarian, self.new_user)

        with self.assertRaises(PermissionError):
            self.library.add_user(self.member, self.new_user)

    def test_only_admin_can_remove_user_if_available(self):
        self.library.add_user(self.admin, self.new_user)
        if self.new_user.username in self.library.users_catalog:
            self.library.remove_user(self.admin, self.new_user.username)
            self.assertNotIn(self.new_user.username, self.library.users_catalog)
        else:
            self.fail("User is not in the catalog")

    def test_librarian_cannot_remove_user(self):
        self.library.add_user(self.admin, self.new_user)
        with self.assertRaises(PermissionError):
            self.library.remove_user(self.librarian, self.new_user.username)

    def test_member_cannot_remove_user(self):
        self.library.add_user(self.admin, self.new_user)
        with self.assertRaises(PermissionError):
            self.library.remove_user(self.member, self.new_user.username)


if __name__ == '__main__':
    unittest.main()
