import time
import random
import string
import subprocess
from os import environ

from loguru import logger
from dotenv import load_dotenv

from fastapi import FastAPI, Request

from api.user import user
from api.movie import movie
from api.auth import auth

# env configuration
load_dotenv(".env")

shell_command = f"unset PICCOLO_CONF; export PICCOLO_CONF={environ.get('PICCOLO_CONF')}"
subprocess.Popen(
    shell_command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# main app
app = FastAPI(title="VTS Interview")


# middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = f"{process_time:.2f}"
    logger.info(
        f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}",
    )

    return response


# routers definition
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(movie.router)


# main root url
@app.get("/")
async def root():
    return {"message": "Hello VTS!"}
