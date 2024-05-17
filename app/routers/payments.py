import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.payment import (
    create_payment,
    delete_payment,
    get_payment,
    get_payments,
    update_payment,
)
from app.db.session import get_db
from app.schemas.payment import Payment, PaymentCreate

router = APIRouter()


@router.get("/payments/", response_model=List[Payment])
def read_payments(
    skip: int = 0,
    limit: int = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10)),
    db: Session = Depends(get_db),
):
    payments = get_payments(db, skip=skip, limit=limit)
    return payments


@router.post("/payments/", response_model=Payment)
def create_payment_endpoint(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db=db, payment=payment)


@router.get("/payments/{payment_id}", response_model=Payment)
def read_payment(payment_id: uuid.UUID, db: Session = Depends(get_db)):
    db_payment = get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


@router.delete("/payments/{payment_id}", response_model=Payment)
def delete_payment_endpoint(payment_id: uuid.UUID, db: Session = Depends(get_db)):
    db_payment = delete_payment(db=db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


@router.put("/payments/{payment_id}", response_model=Payment)
def update_payment_endpoint(
    payment_id: uuid.UUID,
    payment: PaymentCreate,
    db: Session = Depends(get_db),
):
    db_payment = update_payment(
        db=db,
        payment_id=payment_id,
        payment_update=payment,
    )
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
