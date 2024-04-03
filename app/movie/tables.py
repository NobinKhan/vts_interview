from enum import Enum
from decimal import Decimal
from piccolo.table import Table
from piccolo.columns.column_types import Decimal as DecimalField, Varchar, Date, ForeignKey
from app.auth.tables import AuthUser

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


class Rating(Table, tablename="rating"):
    user_id = ForeignKey(references=AuthUser)
    movie_id = ForeignKey(references=Movie)
    rating = DecimalField(digits=(2, 1), default=Decimal(0.0), required=True, null=True)
