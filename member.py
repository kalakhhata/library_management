from book import Book
class Member:
    def __init__(self,member_id,name,email):
        self.member_id=member_id
        self.name=name
        self.email=email
        self.borrowed_books=[]
    
    def borrow_book(self,book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
    
    def return_book(self,book):
        if book.mark_as_returned():
            self.borrowed_books.remove(book)
    
    def __str__(self):
        book_title = [book.title for book in self.borrowed_books]
        formated_title = ",".join(book_title)
        return f"Member ID: {self.member_id} | Name : {self.name} | Email : {self.email} | Borrowed Books : {formated_title}"






        




            


            
