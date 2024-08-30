import unittest
from datetime import datetime
from main.Book import Book


class BookTest(unittest.TestCase):

    def test_should_throw_exception_when_isbn_is_null(self):
        with self.assertRaises(ValueError) as context:
            Book(None, "Clean Code", "Robert Cecil Martin", 1234,datetime(2012, 1, 1), 1998, 3)
        self.assertEqual(str(context.exception), "ISBN should not be null or empty")

    def test_should_throw_exception_when_title_is_null(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", None, "Robert Cecil Martin", 1234,datetime(2012, 1, 1),1998,3)
        self.assertEqual(str(context.exception), "Title should not be null or empty")

    def test_should_throw_exception_when_author_is_empty(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", "Clean Code", "",1234, datetime(2012, 1, 1),1998,3)
        self.assertEqual(str(context.exception), "Author should not be null or empty")

    def test_should_throw_exception_when_publication_year_is_null(self):
        with self.assertRaises(ValueError) as context:
            Book("9780132350884", "Clean Code", "Robert Cecil Martin", None,None,3)
        self.assertEqual(str(context.exception), "Publication year should not be null")


if __name__ == '__main__':
    unittest.main()
