# -*- coding: utf-8 -*-

from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    fullname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class FileBase(BaseModel):
    file_path: str