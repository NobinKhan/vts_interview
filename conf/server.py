import subprocess
from os import environ

from dotenv import load_dotenv
from fastapi import FastAPI

from api.user import user
from api.movie import movie
from api.auth import auth


load_dotenv(".env")

shell_command = f"unset PICCOLO_CONF; export PICCOLO_CONF={environ.get('PICCOLO_CONF')}"
subprocess.Popen(
    shell_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(movie.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
