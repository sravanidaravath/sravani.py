from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def show(self):
        pass
class Member(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__books = []      
    def borrow(self, book):
        self.__books.append(book)

    def return_book(self, book):
        self.__books.remove(book)

    def show(self):
        print("Member:", self.name)

class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False

class Library:
    def issue(self, member, book):
        if not book.issued:
            book.issued = True
            member.borrow(book)
            print(book.title, "issued.")
        else:
            print("Book already issued.")

    def return_book(self, member, book):
        if book.issued:
            book.issued = False
            member.return_book(book)
            print(book.title, "returned.")
        else:
            print("Book not issued.")
book1 = Book("English")
member1 = Member("sravani")
library = Library()

member1.show()
library.issue(member1, book1)
library.return_book(member1, book1)