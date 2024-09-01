import unittest
from main.Book import Book
from datetime import datetime

class TestBook(unittest.TestCase):
    def test_should_throw_exception_when_isbn_is_null(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", "Clean Code", "Robert Cecil Martin", None, 2012, 3)
        self.assertEqual(str(context.exception), "ISBN_no cannot be null")

    def test_should_throw_exception_when_author_is_empty(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", "Clean Code", "", "1234", 2012, 3)
        self.assertEqual(str(context.exception), "Author cannot be null")

    def test_should_throw_exception_when_title_is_null(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", None, "Robert Cecil Martin", "1234", 2012, 3)
        self.assertEqual(str(context.exception), "Title cannot be null")

    def test_should_throw_exception_when_publication_year_is_null(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", "Clean Code", "Robert Cecil Martin", "1234", None, 3)
        self.assertEqual(str(context.exception), "Publication year cannot be null")

if __name__ == '__main__':
    unittest.main()
