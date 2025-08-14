class Book:
    def __init__(self,book_id,title,author,category):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.category=category
        self.available=True
    
    def mark_as_borrowed(self):
        if self.available:
            self.available=False
            print(f"{self.title} is Borrowed Successfully")
            return True
        else:
            print(f"{self.title} is already Borrowed")
            return False
    
    def mark_as_returned(self):
        if not self.available:
            self.available=True
            print(f"{self.title} is Returned Successfully")
            return True
        else:
            print(f"{self.title} is not Borrowed by anyone")
            return False
    
    def __str__(self):
        isAvailable = "Available" if self.available else "Unavailable"
        return f"Book ID : {self.book_id} | Title : {self.title} | Author : {self.author} | Category : {self.category} | Availablity : {isAvailable}"



    