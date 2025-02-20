from enum import Enum

# storing genre as an enum gives the developer control over which genres to allow
# helps to eliminate duplicate genres from creeping into your storage

class Genre(Enum):
    AUTOBIOGRAPHY = "Autobiography"
    FICTION = "Fiction"
    FILM = "FILM"
    NON_FICTION = "Non-Fiction"
    NOVEL = "Novel"
    PLAY = "Play"

    @classmethod
    def from_string(cls, genre_str):
        for genre in cls:
            if genre.value.lower() == genre_str.lower():
                return genre
        raise ValueError(f"Invalid genre: {genre_str}")