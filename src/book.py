class Book:
    def __init__(self, 
                 title: str, 
                 author: str, 
                 isbn: str,
                 genre: list[str],
                 year_published: int,
                 number_of_pages: int,
                 margin_notes=[],
                 have_read=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.year_published = year_published
        self.number_of_pages = number_of_pages
        self.margin_notes = margin_notes
        self.have_read = have_read
        
    def add_note(self, note: str):
        self.margin_notes.append()

    def mark_as_read_toggle(self):
        if self.have_read:
            self.have_read = False
        else:
            self.have_read = True
        
    def __str__(self):

        read_status = ""
        if self.have_read:
            read_status = "Read"
        else:
            read_status = "Not read"

        return (f"{self.title} by {self.author} ({self.isbn}, Genre: {', '.join(self.genre)}, "
                f"Published: {self.year_published}, Pages: {self.number_of_pages}, Status: {read_status})")
