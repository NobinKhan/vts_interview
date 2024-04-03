from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from app.auth.tables import AuthUser


router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    users = await AuthUser.select().output()
    return ORJSONResponse(users)


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
