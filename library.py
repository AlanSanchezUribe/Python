class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print (f"The Book {self.title} has been borrowed")
        else:
            print (f"The Book {self.title} is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print (f"The Book {self.title} has been returned")
        else:
            print (f"The Book {self.title} is already available")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books_borrowed = [] 

    def borrowed_books(self, book):
        if book.available:
            book.borrow()
            self.books_borrowed.append(book)
        else:
            print ("try another book")
        
    def return_books(self, book):
        if book in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book)
        else:
            print ("You have not borrowed this book")   

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print (f"The Book {book.title} has been added to the library")

    def add_user(self, user):
        self.users.append(user)
        print (f"The User {user.name} has been added to the library")

    def display_books(self):
        print("Books in the library are:")
        for book in self.books:
            if book.available:
                print (f"{book.title} by {book.author}")  

    def display_users(self):
        print("Users in the library are:")
        for user in self.users:
            print (f"{user.name} with user id {user.user_id}")


# Create some books and users
book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("The Da Vinci Code", "Dan Brown")
book3 = Book("The Kite Runner", "Khaled Hosseini")
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")

user1 = User("Alice", 1)
user2 = User("Bob", 2)
user3 = User("Alan", 3) 

# Add books and users to the library
library = Library("Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.add_user(user1)
library.add_user(user2)
library.add_user(user3)

# Display books and users in the library
library.display_books()
library.display_users()

# Borrow and return books
user1.borrowed_books(book1)
user1.borrowed_books(book2)

# Display books and users in the library
library.display_books()

# Return books
user1.return_books(book1)
user1.return_books(book2)

# Display books and users in the library
library.display_books()