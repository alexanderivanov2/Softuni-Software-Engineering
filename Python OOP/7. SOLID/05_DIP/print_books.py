class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class HalfFormatter:
    def format(self, book: Book):
        return book.content[:len(book.content) // 2]


class Printer:
    def get_book(self, book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


book_one = Book("1234567890")
print(Printer().get_book(book_one, HalfFormatter()))
print(Printer().get_book(book_one, Formatter()))
