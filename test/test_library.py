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


if __name__ == '__main__':
    unittest.main()
