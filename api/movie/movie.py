from datetime import datetime, timezone
from decimal import Decimal
from asyncpg import UniqueViolationError
from authx import AuthX
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel, validator

from api.dependency import get_token_header, config
from app.auth.tables import AuthUser
from app.movie.tables import Movie, Rating


router = APIRouter(
    prefix="/api/v1/movie",
    tags=["movie"],
    dependencies=[Depends(get_token_header)],
)


class CreateMovie(BaseModel):
    name: str
    genre: Movie.Genre
    rating: Movie.Rating
    release_date: datetime

    @validator("release_date", pre=True, always=True)
    def pre_release_date(cls, value, values):
        datetime_obj = datetime.strptime(value, "%d-%m-%Y")
        return datetime_obj


class CreateMovieRating(BaseModel):
    rating: Decimal


@router.post("/create/", status_code=201)
async def create_movie(data: CreateMovie):
    # create mvoie
    try:
        await Movie(**data.model_dump()).save()
    except Exception:
        raise HTTPException(status_code=400, detail={"message": "Something went wrong"})
    return ORJSONResponse(
        status_code=201, content={"message": "Movie created successfully"}
    )


@router.get("/all/")
async def get_movies():
    movies: list = (
        await Movie.select()
        .columns(
            Movie.id,
            Movie.name,
            Movie.genre,
            Movie.rating,
            Movie.release_date,
        )
        .order_by(Movie.id)
        .output()
    )
    return ORJSONResponse(movies)


@router.post("/{movie_id}/rate/", status_code=201)
async def create_rate(movie_id: int, data: CreateMovieRating, request: Request):
    payload = await AuthX(config=config).access_token_required(request)
    user = await AuthUser.objects().where(AuthUser.id == int(payload.sub)).first()

    # create rating
    try:
        await Rating(user_id=user.id, movie_id=movie_id, rating=data.rating).save()
    except UniqueViolationError:
        raise HTTPException(
            status_code=400, detail={"message": "You have already rated this movie!"}
        )
    except Exception:
        raise HTTPException(status_code=400, detail={"message": "something went wrong"})

    return ORJSONResponse(
        status_code=201, content={"message": "Movie Rating created successfully"}
    )
