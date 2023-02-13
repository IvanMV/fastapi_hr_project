from pydantic import BaseModel
from pydantic import EmailStr


# данные для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# данные для ответа после создания пользователя
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
