from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

class LoginData(BaseModel):
    username: str
    password: str | None = None


@router.post("/login/")
async def login(data: LoginData):
    print(data)
    return {"message": "Item created"}
