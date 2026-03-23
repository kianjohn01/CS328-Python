class Book:
    def __init__(self, title, author, isbn):
        """Initializes the book attributes."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

if __name__ == "__main__":

    my_book = Book("The handy philosophy answer book", " Naomi Zack", "1578592267")
    

    print(my_book)
