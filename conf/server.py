from fastapi import FastAPI

from api.user import user
from api.movie import movie
from api.auth import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(movie.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
