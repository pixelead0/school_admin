import uuid

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging_config import logger
from app.models.school import School
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: uuid.UUID):
    logger.info(user_id)
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, db_user: User, user_update: UserUpdate):
    if user_update.password:
        db_user.hashed_password = pwd_context.hash(user_update.password)
    db_user.username = user_update.username or db_user.username
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: uuid.UUID):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
