import unittest
from book import Book, Genre

class TestBook(unittest.TestCase):

    def test_create_book(self):
        """Test book creation with multiple genres and default values."""
        book = Book(
            "1984", "George Orwell", "123456789",
            [Genre.FICTION, Genre.SCIENCE], 1949, 328
        )

        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.isbn, "123456789")
        self.assertEqual(book.genre, [Genre.FICTION, Genre.SCIENCE])
        self.assertEqual(book.year_published, 1949)
        self.assertEqual(book.number_of_pages, 328)
        self.assertEqual(book.margin_notes, [])
        self.assertFalse(book.have_read)

        expected_str = "1984 by George Orwell (ISBN: 123456789, Genre: Fiction, Science, Published: 1949, Pages: 328, Status: Not Read)"
        self.assertEqual(str(book), expected_str)

    def test_add_margin_note(self):
        """Test adding margin notes to a book."""
        book = Book("1984", "George Orwell", "123456789", [Genre.FICTION], 1949, 328)
        
        book.add_note("Great opening line!")
        book.add_note("Foreshadowing in Chapter 2.")

        self.assertEqual(book.margin_notes, ["Great opening line!", "Foreshadowing in Chapter 2."])

    def test_mark_as_read(self):
        """Test marking a book as read."""
        book = Book("1984", "George Orwell", "123456789", [Genre.FICTION], 1949, 328)
        
        book.mark_as_read()
        
        self.assertTrue(book.have_read)

if __name__ == "__main__":
    unittest.main()