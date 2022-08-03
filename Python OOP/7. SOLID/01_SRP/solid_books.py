class Library:
    def __init__(self):
        self.storage = []

    def find_book(self, book):
        try:
            return self.storage[self.storage.index(book)]
        except ValueError:
            return "No such book"

    def add_book(self, book):
        self.storage.append(book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
