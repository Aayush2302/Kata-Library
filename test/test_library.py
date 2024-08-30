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

    def test_admin_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.admin,book)
        self.assertIn("003", self.library.books_catalog)

    def test_member_cannot_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        with self.assertRaises(ValueError):
            self.library.add_book(self.member,book) #member cannot add books

    def test_librarian_add_book(self):
        book = Book("003", "Death Note", "Light Yagami", "300", 2010, 5)
        self.library.add_book(self.librarian,book)
        self.assertIn("003", self.library.books_catalog)

if __name__ == '__main__':
    unittest.main()
