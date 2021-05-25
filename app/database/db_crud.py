from sqlalchemy.orm import Session

from . import db_models, db_schemas


def get_user(db: Session, user_id: int):
    return db.query(db_models.User).filter(db_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(db_models.User).filter(db_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: db_schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = db_models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Location).offset(skip).limit(limit).all()


def create_user_location(db: Session, location: db_schemas.LocationCreate, user_id: int):
    db_location = db_models.Location(**location.dict(), owner_id=user_id)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
