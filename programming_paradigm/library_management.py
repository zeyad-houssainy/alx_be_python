class Book:
    def __init__(self, title, author):
        # verification 
        if title == None or author == None:
            raise ValueError("Both title and author must have values")
        # Initialization
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout_book(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    # Check if book avaiilable 
    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"{self.title} by {self.author}"
        

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, new_book):
        # verify you add a book object
        if isinstance(new_book, Book):
            self._books.append(new_book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title and book.is_available():
                book.checkout_book()
                break

    def return_book(self, title):
        for book in self._books:
            if title == book.title and not book.is_available():
                book.return_book()
                break
    
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book)

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("")
    print("Available books after setup:") #Available books after setup:
    library.list_available_books()  # Brave New World by Aldous Huxley
                                    #1984 by George Orwell

    # Simulate checking out a book
    print("")
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':") #Available books after checking out '1984':
    library.list_available_books()  # Brave New World by Aldous Huxley


    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()  # Brave New World by Aldous Huxley
                                    # 1984 by George Orwell


if __name__ == "__main__":
    main()


