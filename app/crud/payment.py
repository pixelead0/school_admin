from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate
import uuid
import os

PAGINATION_DEFAULT_LIMIT = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10))

def get_payment(db: Session, payment_id: uuid.UUID):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def get_payments(db: Session, skip: int = 0, limit: int = PAGINATION_DEFAULT_LIMIT):
    return db.query(Payment).offset(skip).limit(limit).all()

def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payment(
        id=uuid.uuid4(),
        student_id=payment.student_id,
        school_id=payment.school_id,
        payment_type_id=payment.payment_type_id
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: uuid.UUID):
    db_payment = get_payment(db, payment_id)
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment

def update_payment(db: Session, payment_id: uuid.UUID, payment_update: PaymentCreate):
    db_payment = get_payment(db, payment_id)
    if db_payment:
        db_payment.student_id = payment_update.student_id
        db_payment.school_id = payment_update.school_id
        db_payment.payment_type_id = payment_update.payment_type_id
        db.commit()
        db.refresh(db_payment)
    return db_payment
