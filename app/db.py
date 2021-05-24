"""Database functions/endpoints."""

import os
from fastapi import APIRouter, Depends, HTTPException
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List



load_dotenv()

# SQLALCHEMY_DATABASE_URL = "sqlite:///temporary.db"
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

router = APIRouter()

from . import db_crud, db_models, db_schemas

@router.get('/info')
async def get_url():
    """Verify we can connect to the database, 
    and return the database URL in this format:
    dialect://user:password@host/dbname

    The password will be hidden with ***
    """
    url_without_password = repr(engine.url)
    return {'database_url': url_without_password}


db_models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=db_schemas.User)
def create_user(user: db_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[db_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=db_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/location/", response_model=db_schemas.Location)
def create_location_for_user(
    user_id: int, location: db_schemas.LocationCreate, db: Session = Depends(get_db)
):
    return db_crud.create_user_location(db=db, location=location, user_id=user_id)


@router.get("/locations/", response_model=List[db_schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = db_crud.get_locations(db, skip=skip, limit=limit)
    return locations
