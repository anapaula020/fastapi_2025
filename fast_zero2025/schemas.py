from pydantic import BaseModel
from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message: str
    
class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    
class UserPublic(BaseModel):
    username: str
    email: str
    
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    username: str
    email: EmailStr

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserDB(UserSchema):
    id: int
    
class UserList(BaseModel):
    users: list[UserPublic]
