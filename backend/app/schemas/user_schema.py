from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    address: str | None = None

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    address: str | None = None