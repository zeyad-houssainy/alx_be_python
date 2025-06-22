class Book:
    # initialize with verification
    def __init__(self, title, author):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("title must be a string")
        if isinstance(author, str):
            self.author = author
        else:
            raise TypeError("author must be a string")

    def __str__(self):
        return (f"{self.title} by {self.author}")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        if isinstance(file_size, int):
            self.file_size = file_size
        else:
            raise TypeError("file_size must be an integer")

    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            raise TypeError("page_count must be an integer.")
    
    def __str__(self):
        return f"PrintBook: {super().__str__()}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("book must be an instance of Book class")
    
    def list_books(self):
        for book in self.books:
            print(book)