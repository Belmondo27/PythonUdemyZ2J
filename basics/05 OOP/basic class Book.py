class Book:
    def __init__(self, author, title, isbn , year = "unknow"):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year
    
    def printData(self):
        print(self.author, self.title, self.isbn, self.year)

    


book1 = Book("Ola Kowalska", "Podróże", 2020)
book1.isbn = 100
book1.printData()