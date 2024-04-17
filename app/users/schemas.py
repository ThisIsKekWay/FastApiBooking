from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    pwd: str