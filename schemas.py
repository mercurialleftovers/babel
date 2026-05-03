from pydantic import (BaseModel, EmailStr, ConfigDict, Field, )
from typing import Annotated
from enum import Enum
from datetime import datetime, UTC

class Role(Enum):
    OPERATOR = "operator"
    TECHNICIAN = "technician"
    ENGINEER = "engineer"

class UserResponse(BaseModel):
    username: str = Field(min_length=6, max_length=25)
    role: Role
    email: EmailStr
    

class UserCreate(UserResponse):
    password: str = Field(min_length=8, max_length=40)
    image_path: str = Field(min_length=8, max_length=20)

