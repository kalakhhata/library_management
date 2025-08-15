from library import Library
from book import Book
from member import Member
from librarian import Librarian

def main():
    # Create Library
    lib = Library()

    # Create Librarian
    librarian = Librarian("S001", "Alice", "alice@library.com")

    # Create Books
    book1 = Book("B001", "1984", "George Orwell", "Fiction")
    book2 = Book("B002", "Python Basics", "John Doe", "Programming")

    # Add Books
    librarian.add_book(book1, lib)
    librarian.add_book(book2, lib)

    # Create Member
    member1 = Member("M001", "Bob", "bob@email.com")
    librarian.add_member(member1, lib)

    # List all books
    lib.list_all_books()

    # Borrow book
    member1.borrow_book(book1)

    # List available books
    lib.list_available_books()

    # Return book
    member1.return_book(book1)

    # List available books again
    lib.list_available_books()

    # List All Members
    lib.list_all_members()

if __name__ == "__main__":
    main()
