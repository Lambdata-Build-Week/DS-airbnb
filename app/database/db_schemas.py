from typing import List, Optional

from pydantic import BaseModel


class LocationBase(BaseModel):
    title: str
    description: Optional[str] = None


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    locations: List[Location] = []

    class Config:
        orm_mode = True
