# Pyton
from ast import Pass
from datetime import date
from uuid import UUID
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class PasswordMixin(BaseModel):   # Creamos este nuevo modelo
    password: str = Field(...,
                          min_length=8,
                          max_length=64,
                          example='password',)

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50

    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class UserLogin(PasswordMixin, UserBase):
    pass


class UserRegister(PasswordMixin,User):  
# Utilizamos la herencia de clases para añadir password aquí.
    pass