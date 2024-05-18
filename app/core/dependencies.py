from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud
from app.schemas.token import TokenData
from app.core.config import settings
from app.core.security import decode_access_token
from app.core.logging_config import logger
from app.db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        logger.info(payload)
        if payload is None:
            raise credentials_exception
        token_data = TokenData(**payload)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = crud.user.get_user_by_username(db, username=token_data.sub)
    if user is None:
        raise credentials_exception
    return user
