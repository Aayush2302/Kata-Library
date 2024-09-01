import unittest
import os
import HtmlTestRunner

from main.Book import Book
from main.Library import Library
from main.User import User


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Setting up the initial conditions for the tests
        self.admin = User(username="admin_user", role="Admin")
        self.librarian = User(username="librarian", role="Librarian")
        self.member1 = User(username="Alex", role="Member")
        self.member2 = User(username="Allen", role="Member")
        self.member3 = User(username="Bob", role="Member")
        self.library = Library()

    def test_add_books(self):
        book1 = Book("001", "Death Note", "Light Yagami", "100", 2010, 3)
        book2 = Book("002", "Super-man", "DC", "200", 2000, 2)
        book3 = Book("003", "Spider-man", "Marvel-Comics", "300", 2004, 1)

        self.library.add_book(self.admin, book1)
        self.library.add_book(self.librarian, book2)
        self.library.add_book(self.admin, book3)

        # Asserting that the books were added
        self.assertIn("001", self.library.books_catalog)
        self.assertIn("002", self.library.books_catalog)
        self.assertIn("003", self.library.books_catalog)

    def test_add_users(self):
        self.library.add_user(self.admin, self.member1)
        self.library.add_user(self.admin, self.member2)
        self.library.add_user(self.admin, self.member3)

        # Asserting that the users were added
        self.assertIn("Alex", self.library.users_catalog)
        self.assertIn("Allen", self.library.users_catalog)
        self.assertIn("Bob", self.library.users_catalog)

    def test_borrow_books(self):
        # Setup the books
        book1 = Book("001", "Death Note", "Light Yagami", "100", 2010, 3)
        book2 = Book("002", "Super-man", "DC", "200", 2000, 2)
        book3 = Book("003", "Spider-man", "Marvel-Comics", "300", 2004, 1)

        self.library.add_book(self.admin, book1)
        self.library.add_book(self.librarian, book2)
        self.library.add_book(self.admin, book3)

        # Setup the users
        self.library.add_user(self.admin, self.member1)
        self.library.add_user(self.admin, self.member2)

        # Members borrowing books
        self.library.borrow_book(self.member1, "002")
        self.library.borrow_book(self.member2, "003")

        # Asserting that the stock is updated correctly
        self.assertEqual(self.library.books_catalog["002"].stock, 1)
        self.assertEqual(self.library.books_catalog["003"].stock, 0)

    def test_return_books(self):
        # Setup the books and users
        self.test_borrow_books()

        # Members returning books
        self.library.return_book(self.member1, "002")
        self.library.return_book(self.member2, "003")

        # Asserting that the stock is updated correctly
        self.assertEqual(self.library.books_catalog["002"].stock, 2)
        self.assertEqual(self.library.books_catalog["003"].stock, 1)

    def test_view_available_books(self):
        # Setup the books
        book1 = Book("001", "Death Note", "Light Yagami", "100", 2010, 3)
        book2 = Book("002", "Super-man", "DC", "200", 2000, 2)
        book3 = Book("003", "Spider-man", "Marvel-Comics", "300", 2004, 1)

        self.library.add_book(self.admin, book1)
        self.library.add_book(self.librarian, book2)
        self.library.add_book(self.admin, book3)

        # Mock the print function to capture output
        # with unittest.mock.patch('builtins.print') as mocked_print:
        #     self.library.view_available_books()
        #     # You can check that the correct prints are called
        #     mocked_print.assert_any_call("Identifier: 001, Title:Death Note, Author:Light Yagami, Stock:3")
        #     mocked_print.assert_any_call("Identifier: 002, Title:Super-man, Author:DC, Stock:2")
        #     mocked_print.assert_any_call("Identifier: 003, Title:Spider-man, Author:Marvel-Comics, Stock:1")


if __name__ == "__main__":
    # Create the report output directory if not exists
    output_dir = os.path.join(os.getcwd(), 'test_report')
    if not os.path.exists(output_dir):
        pass
    os.makedirs(output_dir)

    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output=output_dir),
        verbosity=2)
