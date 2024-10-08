from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    hashed_password: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str
