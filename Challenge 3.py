
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"Ebook: {self.title} by {self.author} ({self.file_size}MB)"


class Library:
    def __init__(self):
        self.books = []
        self.index = 0

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


if __name__ == "__main__":
    library = Library()


    library.add_book(Book("The handy philosophy answer book", " Naomi Zack"))
    library.add_book(Ebook("The Mountain Is You", "Brianna Wiest", 20))


    print("Library Collection:\n")


    for item in library:
        print(item)
