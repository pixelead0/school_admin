# -*- coding: utf-8 -*-
import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.payment_type import (create_payment_type, delete_payment_type,
                                   get_payment_type, get_payment_types,
                                   update_payment_type)
from app.db.session import get_db
from app.schemas.payment_type import PaymentType, PaymentTypeCreate

router = APIRouter()


@router.get("/payment_types/", response_model=List[PaymentType])
def read_payment_types(skip: int = 0, limit: int = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10)), db: Session = Depends(get_db)):
    payment_types = get_payment_types(db, skip=skip, limit=limit)
    return payment_types


@router.post("/payment_types/", response_model=PaymentType)
def create_payment_type_endpoint(payment_type: PaymentTypeCreate, db: Session = Depends(get_db)):
    return create_payment_type(db=db, payment_type=payment_type)


@router.get("/payment_types/{payment_type_id}", response_model=PaymentType)
def read_payment_type(payment_type_id: uuid.UUID, db: Session = Depends(get_db)):
    db_payment_type = get_payment_type(db, payment_type_id=payment_type_id)
    if db_payment_type is None:
        raise HTTPException(status_code=404, detail="Payment type not found")
    return db_payment_type


@router.delete("/payment_types/{payment_type_id}", response_model=PaymentType)
def delete_payment_type_endpoint(payment_type_id: uuid.UUID, db: Session = Depends(get_db)):
    db_payment_type = delete_payment_type(
        db=db, payment_type_id=payment_type_id)
    if db_payment_type is None:
        raise HTTPException(status_code=404, detail="Payment type not found")
    return db_payment_type


@router.put("/payment_types/{payment_type_id}", response_model=PaymentType)
def update_payment_type_endpoint(payment_type_id: uuid.UUID, payment_type: PaymentTypeCreate, db: Session = Depends(get_db)):
    db_payment_type = update_payment_type(
        db=db, payment_type_id=payment_type_id, payment_type_update=payment_type)
    if db_payment_type is None:
        raise HTTPException(status_code=404, detail="Payment type not found")
    return db_payment_type
