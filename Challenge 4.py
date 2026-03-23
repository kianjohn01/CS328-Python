import mysql.connector


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn})"



class Ebook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        return f"Ebook: {self.title} by {self.author} (ISBN: {self.isbn}, Format: {self.file_format})"



class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def save_book(self, book):
        if isinstance(book, Ebook):
            query = "INSERT INTO books (title, author, isbn, file_format) VALUES (%s, %s, %s, %s)"
            values = (book.title, book.author, book.isbn, book.file_format)
        else:
            query = "INSERT INTO books (title, author, isbn, file_format) VALUES (%s, %s, %s, NULL)"
            values = (book.title, book.author, book.isbn)

        self.cursor.execute(query, values)
        self.connection.commit()

    def load_books(self):
        self.cursor.execute("SELECT title, author, isbn, file_format FROM books")
        rows = self.cursor.fetchall()

        books = []
        for row in rows:
            title, author, isbn, file_format = row
            if file_format:
                books.append(Ebook(title, author, isbn, file_format))
            else:
                books.append(Book(title, author, isbn))
        return books

    def close(self):
        self.cursor.close()
        self.connection.close()



if __name__ == "__main__":
    db = DatabaseManager(
        host="localhost",
        user="root",
        password="",
        database="library_db"
    )


    db.save_book(Book("Python Basics", "John Smith", "1111")) #"The handy philosophy answer book", " Naomi Zack"
    db.save_book(Ebook("AI Guide", "Jane Doe", "2222", "PDF")) #"The Mountain Is You", "Brianna Wiest", 20

    print("Books from Database:\n")

 
    books = db.load_books()
    for book in books:
        print(book)

    db.close()
