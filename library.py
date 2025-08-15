import json
import os
from book import Book
from member import Member
class Library:
    def __init__(self, books_file="data/books.json",members_file="data/members.json"):
        self.books_file=books_file
        self.members_file=members_file
        self.books=[]
        self.members=[]
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, "r") as f:
                books_data = json.load(f)
                self.books = [Book(**b) for b in books_data]
        
        if os.path.exists(self.members_file):
            with open(self.members_file, "r") as f:
                members_data= json.load(f)
                self.members=[Member(**m) for m in members_data]
    
    def save_data(self):
        with open(self.books_file,"w") as f:
            json.dump([b.__dict__ for b in self.books], f , indent=4)
        
        with open(self.members_file,"w") as f:
            json.dump([m.__dict__ for m in self.members], f , indent=4)

    def register_member(self, member):
        for mem in self.members:
            if mem.member_id == member.member_id:
                return False
        return True
    
    def add_book(self,book):
        for b in self.books:
            if b.book_id==book.book_id:
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
    
    def list_all_members(self):
        if not self.members:
            print("No Members in library.")
        for member in self.members:
            print(member)
    
    def list_available_books(self):
        for info in self.books:
            if info.available:
                print(f" Book ID : {info.book_id} | Book Title : {info.title} | Author : {info.author} | Category : {info.category} \n")
    
    