class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
b1 = Book("Harry Potter","J.K.Rowling")
print(f"name of the most popular book : {b1.title}")
print  (f"author:{b1.author}")

