from datetime import timedelta
from fastapi import HTTPException, Request

from authx import AuthX, AuthXConfig

config = AuthXConfig(JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30))
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = "SECRET_KEY"


auth_token = AuthX(config=config)

async def get_token_header(access: Request):
    try:
        await auth_token.access_token_required(access)
    except Exception:
        raise HTTPException(status_code=401, detail={"message": "Bad credentials"})
    


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")