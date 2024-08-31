# class for String validation
class String_validation:
    @staticmethod
    def validate_string(value, message):
        if value is None or value == '':
            raise ValueError(message)


# class Book : identifier,title,author,ISBN_no,publication_year,stock
class Book:
    def __init__(self, identifier, title, author, ISBN_no, publication_year, stock):
        self.validate_require_attribute(identifier, title, author, ISBN_no, publication_year)  #validate every attribute
        self.identifier = identifier
        self.title = title
        self.author = author
        self.ISBN_no = ISBN_no
        self.publication_year = publication_year
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    #validation message with validation
    def validate_require_attribute(self, identifier, title, author, ISBN_no, publication_year):
        String_validation.validate_string(identifier, "Identifier can not be null")
        String_validation.validate_string(title, "Title can not be null")
        String_validation.validate_string(author, "Author can not be null")
        String_validation.validate_string(ISBN_no, "ISBN_no can not be null")
        String_validation.validate_string(publication_year, "Publication year can not be null")

    def update_stock(self, amount):
        if self.stock < amount:
            raise ValueError("Not enough stock to complete the operation")
        self.stock += amount

    def __repr__(self):
        return f"Book(identifier={self.identifier} title={self.title}, author={self.author}), ISBN_no={self.ISBN_no}, publication_year={self.publication_year}, stock={self.stock}, available={self.available})"
