from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, validator, ValidationError

from app.movie.commands._example_data import MOVIES, RATINGS
from app.movie.tables import Movie, Rating


class CreateMovie(BaseModel):
    id: int
    name: str
    genre: Movie.Genre
    rating: Movie.Rating
    release_date: datetime

    @validator("release_date", pre=True, always=True)
    def pre_release_date(cls, value, values):
        datetime_obj = datetime.strptime(value, "%d-%m-%Y")
        return datetime_obj


class CreateMovieRating(BaseModel):
    id: int
    user_id: int
    movie_id: int
    rating: Decimal = Field(gt=-1, le=11)


async def load_data():
    """
    Load some example data into the database.
    """
    for table_class in [Movie, Rating]:
        await table_class.delete(force=True)

    try:
        await Movie.insert(*[Movie(**CreateMovie(**d).model_dump()) for d in MOVIES])
        await Rating.insert(
            *[Rating(**CreateMovieRating(**d).model_dump()) for d in RATINGS],
        )
    except ValidationError as e:
        print(f"Failed to load data: {e.errors()}")

    # We need to update the sequence, as we explicitly set the IDs.
    await Movie.raw("SELECT setval('movie_id_seq', max(id)) FROM movie")
    await Rating.raw("SELECT setval('rating_id_seq', max(id)) FROM rating")
