import csv
from book import Book

class Library():

    def __init__(self,
                library_name: str,
                bookshelf=[],
                currently_reading=None):
        self.library_name = library_name
        self.bookshelf = bookshelf
        self.currently_reading = currently_reading
    
    def add_book(self, book: Book):
        if book not in self.bookshelf:
            self.bookshelf.append(book)

    def add_books_from_csv(self, filename):
        books_from_csv = []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                title = row[0]
                author = row[1]
                isbn = row[2]
                genres = row[3].split('; ')
                year = int(row[4])
                pages = int(row[5])
                if row[6]:
                    notes = row[6].split('; ')
                else:
                    notes = []
                have_read = row[7]
                book = Book(title, author, isbn, genres, year, pages, notes, have_read)
                self.add_book(book)

    def __str__(self):
        bookshelf_str = f"{self.library_name}\n"
        for book in self.bookshelf:
            bookshelf_str += str(book) + '\n'
        return bookshelf_str
    
    # display book details

