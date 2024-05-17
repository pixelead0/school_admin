import os
import uuid
from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models
from app.core.config import settings
from app.core.security import create_access_token
from app.crud.user import (
    create_user,
    get_user,
    get_user_by_username,
    get_users,
)
from app.db.session import get_db
from app.schemas.token import Token
from app.schemas.user import User, UserCreate

router = APIRouter()


@router.post("/login", response_model=Token)
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = crud.user.authenticate_user(
        db,
        username=form_data.username,
        password=form_data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/user/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered",
        )
    return create_user(db=db, user=user)


@router.get("/users/", response_model=List[User])
def read_users(
    skip: int = 0,
    limit: int = settings.PAGINATION_DEFAULT_LIMIT,
    db: Session = Depends(get_db),
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/user/{user_id}", response_model=User)
def read_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
