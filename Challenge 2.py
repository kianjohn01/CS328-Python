class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Ebook(Book):
    def __init__(self, title, author, isbn, file_format):

        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):

        return f"{super().__str__()} - Format: {self.file_format}"


if __name__ == "__main__":
    my_ebook = Ebook("The Mountain Is You", "Brianna Wiest", "9781949759228", "EPUB")
    print(my_ebook)
