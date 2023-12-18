# class Book:
# title,author
# display_details()
# claculate_price()
# class Fiction_book:
#     title,author,genre 
#     display_details()
#     claculate_price()

# class Nonfiction_book:
#     title,author,topic
#     display_details()
#     claculate_price()

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def display_details(self):
        print(f"name of title: {self.title}")
        print(f"name of author: {self.author}")
        
    
    def calcutate_price(self):
        pass

class FictionBook(Book):
    def __init__(self, title, author,genre,price,quantity):
        super().__init__(title, author)
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def display_details(self):
        super().display_details()
        print(f"genre : {self.genre}")
    
    def calcutate_price(self):
        return self.price * self.quantity

class NonfictionBook(Book):
    def __init__(self, title, author,topic,price,quantity):
        super().__init__(title, author)
        self.topic = topic
        self.price = price
        self.quantity = quantity
    
    def display_details(self):
        super().display_details()
        print(f"topic : {self.topic}")
    
    def calcutate_price(self):
        return self.price * self.quantity
        



fiction_book = FictionBook("The Hobbit", "J.R.R. Tolkien", "Fantasy")
nonfiction_book = NonfictionBook("Sapiens", "Yuval Noah Harari", "History")

fiction_book.display_details()
fiction_book.calculate_price()

print("\n")

nonfiction_book.display_details()
nonfiction_book.calculate_price()

    

    





    
        