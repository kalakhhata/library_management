from member import Member
class Librarian(Member):
    def __init__(self,id,name,email):
        super().__init__(id,name,email)
        self.staff_id=id
    def add_member(self,member,library):
        if library.register_member(member):
            library.members.append(member)
            library.save_data()
            print(f"{member.name} has been Registered")
        else:
            print(f"{member.name} has been Registered with Different ID")
    def add_book(self,book,library):
        if library.add_book(book):
            library.books.append(book)
            library.save_data()
            print(f"Librarian {self.name} added '{book.title}' to the library.")
        else:
            print(f"{book.title} already exist with same Book ID")
        
    
    def remove_book(self,book_id,library):
        book_to_remove=None

        for book in library.books:
            if book.book_id ==book_id:
                book_to_remove=book
                break
        
        if book_to_remove:
            library.books.remove(book_to_remove)
            print(f"Librarian {self.name} removed '{book_to_remove.title}' from the library.")
        else:
            print(f"Book with ID {book_id} not found in the library.")