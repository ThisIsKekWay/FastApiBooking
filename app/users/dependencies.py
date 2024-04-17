from fastapi import Depends, Request
from jose import ExpiredSignatureError, JWTError, jwt

from app.config import settings
from app.exceptions import (
    TokenExpiredException,
    TokenFormatIsWrongException,
    TokenIsMissingException,
    UserIsMissingException,
)
from app.users.dao import UsersDAO
from app.users.models import Users


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenIsMissingException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise TokenFormatIsWrongException

    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsMissingException

    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsMissingException
    return user


async def get_current_admin(current_admin: Users = Depends(get_current_user)):
    # if current_admin.role != "admin":
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав")
    return current_admin
