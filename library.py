class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    
    def register_member(self, member):
        for mem in self.members:
            if mem.member_id == member.member_id:
                return False
        return True
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
                return
        print("Book doesn't exist in Database")
    
    def find_book_by_id(self, id):
        for book in self.books:
            if book.book_id == id:
                print(book)
                return
        print("Book doesn't exist in Database")
    
    def list_all_books(self):
        if not self.books:
            print("No books in library.")
        for book in self.books:
            print(book)
    
    def list_available_books(self):
        for info in self.books:
            if info.available:
                print(f" Book ID : {info.book_id} | Book Title : {info.title} | Author : {info.author} | Category : {info.category} \n")
    
    