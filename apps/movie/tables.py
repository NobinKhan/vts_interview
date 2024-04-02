from enum import Enum
from piccolo.table import Table
from piccolo.columns.column_types import Varchar, Date



class Movie(Table, tablename="movie"):
    class Genre(str, Enum):
        action = "Action"
        adventure = "Adventure"
        animation = "Animation"
        biography = "Biography"
        comedy = "Comedy"
        crime = "Crime"
        documentary = "Documentary"
        drama = "Drama"
        family = "Family"
        fantasy = "Fantasy"
        film_noir = "Film-Noir"
        history = "History"
        horror = "Horror"
        music = "Music"
        musical = "Musical"
        mystery = "Mystery"
        romance = "Romance"
        science_fiction = "Science-Fiction"
        sport = "Sport"
        superhero = "Superhero"
        thriller = "Thriller"
        war = "War"
        western = "Western"

    class Rating(str, Enum):
        g = "G"
        pg = "PG"
        pg_13 = "PG-13"
        r = "R"
        nc_17 = "NC-17"

    name = Varchar(length=50, unique=True, required=True, null=True)
    genre = Varchar(length=20, choices=Genre, unique=False, required=True, null=True)
    rating = Varchar(length=8, choices=Rating, unique=False, required=True, null=True)
    release_date = Date(required=True, null=True)
