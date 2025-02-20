import json
import os
from src.book import Book
from src.genre import Genre

class Library:
    def __init__(self, name):
        """Initializes a Library and loads books if a save file exists."""
        self.name = name
        self.books = []
        self.filename = f"{name.lower().replace(' ', '_')}.txt"  # Save as a text file
        self.load_library()  # Load books from file if exists

    def add_book(self, book: Book):
        """Adds a book to the library and saves the update."""
        self.books.append(book)
        self.save_library()

    def remove_book(self, isbn: str):
        """Removes a book by ISBN and saves the update."""
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_library()

    def save_library(self):
        """Saves the library to a text file in JSON format."""
        data = {
            "library_name": self.name,
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "genre": [g.value for g in book.genre],  # Convert Enum to string
                    "year_published": book.year_published,
                    "number_of_pages": book.number_of_pages,
                    "margin_notes": book.margin_notes,
                    "have_read": book.have_read
                }
                for book in self.books
            ]
        }
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_library(self):
        """Loads the library from a text file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [
                    Book(
                        b["title"], 
                        b["author"], 
                        b["isbn"], 
                        [Genre(g) for g in b["genre"]],  # Convert string to Enum
                        b["year_published"], 
                        b["number_of_pages"], 
                        b["margin_notes"], 
                        b["have_read"]
                    ) for b in data["books"]
                ]

    def list_books(self):
        """Returns a list of books in the library."""
        return [str(book) for book in self.books]