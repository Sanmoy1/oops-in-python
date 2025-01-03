# Step 1: Create small components (e.g., Book class).
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"The book '{self.title}' is checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")

# Step 2: Create another small component (e.g., Member class).
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_checked_out:
            self.borrowed_books.append(book)
            book.checkout()
        else:
            print(f"Sorry, the book '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"{self.name} does not have the book '{book.title}'.")

# Step 3: Integrate components into a larger system (Library class).
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}' by {book.author}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")

    def display_books(self):
        print("\nAvailable books in the library:")
        for book in self.books:
            status = "Available" if not book.is_checked_out else "Checked Out"
            print(f"- {book.title} by {book.author} (Status: {status})")

# Step 4: Use the integrated system.
if __name__ == "__main__":
    # Create a library
    my_library = Library("City Library")
    
    # Add books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "0987654321")
    my_library.add_book(book1)
    my_library.add_book(book2)

    # Add a member
    member1 = Member("Alice", "M001")
    my_library.add_member(member1)

    # Interact with the library system
    my_library.display_books()
    member1.borrow_book(book1)
    my_library.display_books()
    member1.return_book(book1)
    my_library.display_books()
    
