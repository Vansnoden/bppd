# -*- coding: utf-8 -*-

import json
import os
import shutil
from sqlalchemy import and_
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from pathlib import Path
import datetime
from enum import Enum
from pprint import pprint
import re, os
import shutil
import pandas as pd
import openpyxl , csv

from tqdm import tqdm
import traceback
import warnings
import uuid
import geopandas as gpd
from shapely.geometry import Point

DELIMITER = ","

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 0):
    if skip and limit:
        return db.query(models.User).offset(skip).limit(limit).all()
    else:
        return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    db_user = models.User(
        username=user.username,
        email=user.email, 
        fullname=user.fullname,
        is_active=True,
        hashed_password=pwd_context.hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    res = db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return res


def upload_data_from_file(filepath) -> bool:
    
    return False