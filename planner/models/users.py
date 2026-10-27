from typing import Optional, List
from pydantic import BaseModel, EmailStr
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "kumushbaeva@example.com",
                "password": "StrongPass123!",
                "events": []
            }
        }


class NewUser(User):
    pass


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "kumushbaeva@example.com",
                "password": "StrongPass123!"
            }
        }