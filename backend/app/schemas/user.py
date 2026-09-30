from pydantic import BaseModel , EmailStr , Field


class UserCreate(BaseModel):
    name:str = Field(min_length=3 , max_length=100)
    email : EmailStr
    password:str = Field(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    name:str | None = Field(
        default= None , 
        min_length=3 , 
        max_length=100
        )
    email : EmailStr | None = None
    is_active:bool | None = None

class UserResponse(BaseModel):
    id:str
    name:str
    email:str
    is_active:bool
    is_email_verified:bool