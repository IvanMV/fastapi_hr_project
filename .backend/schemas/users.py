from typing import Optional
from pydantic import BaseModel, EmailStr

# данные для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
