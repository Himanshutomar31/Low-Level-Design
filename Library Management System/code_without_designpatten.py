class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"


class User:
    def __init__(self, name):
        self.name = name

    def borrowBook(self, book):
        if book.available:
            book.available = False
            print(f"{self.name} has borrowed the book: {book}")
        else:
            print("The book is not available for borrowing.")

    def returnBook(self, book):
        if not book.available:
            book.available = True
            print(f"{self.name} has returned the book: {book}")
        else:
            print("The book has already been returned.")


class LibrarySystem:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book is not in the library.")

    def displayBooks(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)


# Usage example
library = LibrarySystem()

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.addBook(book1)
library.addBook(book2)

library.displayBooks()

book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.addBook(book3)

library.displayBooks()

user1 = User("Alice")
user2 = User("Bob")

user1.borrowBook(book1)
user2.borrowBook(book2)
user1.borrowBook(book2)

user1.returnBook(book1)
user2.returnBook(book2)

library.displayBooks()
