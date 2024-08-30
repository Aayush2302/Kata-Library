from main.Book import Book


class Library:
    def __init__(self):
        self.books_catalog = {}  # Dictionary to hold books

    def add_book(self, book: Book):
        if book.identifier in self.books_catalog:
            raise ValueError("A Book with this identifier already exists ")
        self.books_catalog[book.identifier] = book


if __name__ == "__main__":
    library = Library()
    book1 = Book("001", "Death Note", "Light Yagami", "100", 2010, 5)
    book2 = Book("002", "Death Note", "Light Yagami", "100", 2010, 5)

    library.add_book(book1)
    library.add_book(book2)