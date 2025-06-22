# from library_system import Book, EBook, PrintBook, Library


# def main():
#     # Create a Library instance
#     my_library = Library()

#     # Create instances of each type of book
#     classic_book = Book("Pride and Prejudice", "Jane Austen")
#     digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
#     paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

#     # Add books to the library
#     my_library.add_book(classic_book)
#     my_library.add_book(digital_novel)
#     my_library.add_book(paper_novel)

#     # List all books in the library
#     my_library.list_books()


# if __name__ == "__main__":
#     main()


# Book: Pride and Prejudice by Jane Austen
# EBook: Snow Crash by Neal Stephenson, File Size: 500KB
# PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234

# from class_static_methods_demo import Calculator
# from polymorphism_demo import Shape, Rectangle, Circle
# import math


# def main():
#     shapes = [
#         Rectangle(10, 5),
#         Circle(7)
#     ]

#     for shape in shapes:
#         print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


# if __name__ == "__main__":
#     main()


# The area of the Rectangle is : 50
# The area of the Circle is : 153.93804002589985

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    main()
