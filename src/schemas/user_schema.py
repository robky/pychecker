from pydantic import BaseModel, EmailStr, field_validator

from services.hash_pwd import get_password_hash


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def hash_password(cls, value):
        return get_password_hash(value)


class UserInDB(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    pass

    class Config:
        orm_mode = True
