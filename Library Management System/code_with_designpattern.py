from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"


class LibrarySystem:
    _instance = None

    @staticmethod
    def getInstance():
        if not LibrarySystem._instance:
            LibrarySystem._instance = LibrarySystem()
        return LibrarySystem._instance

    def __init__(self):
        self.books = []
        self.observers = []

    def addBook(self, book):
        self.books.append(book)
        self.notifyObservers("Book added: " + str(book))

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            self.notifyObservers("Book removed: " + str(book))
        else:
            print("Book is not in the library.")

    def displayBooks(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)

    def registerObserver(self, observer):
        self.observers.append(observer)

    def unregisterObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received notification: {message}")


# Usage example
library = LibrarySystem.getInstance()

user1 = User("Alice")
user2 = User("Bob")

library.registerObserver(user1)
library.registerObserver(user2)

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.addBook(book1)
library.addBook(book2)

library.displayBooks()

book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.addBook(book3)

library.removeBook(book2)

library.unregisterObserver(user2)

library.removeBook(book1)
