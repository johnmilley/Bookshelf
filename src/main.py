from book import Book
from library import Library

def add_book():
    pass

def load_library():
    pass

def main():
    l = Library("Happy Little Library")

    l.add_books_from_csv('books.csv')

    print(l)
    


if __name__ == "__main__":
    main()