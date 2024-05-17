from sqlalchemy.orm import Session
from app.models.payment_type import PaymentType
from app.schemas.payment_type import PaymentTypeCreate
import uuid
import os

PAGINATION_DEFAULT_LIMIT = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10))

def get_payment_type(db: Session, payment_type_id: uuid.UUID):
    return db.query(PaymentType).filter(PaymentType.id == payment_type_id).first()

def get_payment_types(db: Session, skip: int = 0, limit: int = PAGINATION_DEFAULT_LIMIT):
    return db.query(PaymentType).offset(skip).limit(limit).all()

def create_payment_type(db: Session, payment_type: PaymentTypeCreate):
    db_payment_type = PaymentType(
        id=uuid.uuid4(),
        name=payment_type.name,
        price=payment_type.price
    )
    db.add(db_payment_type)
    db.commit()
    db.refresh(db_payment_type)
    return db_payment_type

def delete_payment_type(db: Session, payment_type_id: uuid.UUID):
    db_payment_type = get_payment_type(db, payment_type_id)
    if db_payment_type:
        db.delete(db_payment_type)
        db.commit()
    return db_payment_type

def update_payment_type(db: Session, payment_type_id: uuid.UUID, payment_type_update: PaymentTypeCreate):
    db_payment_type = get_payment_type(db, payment_type_id)
    if db_payment_type:
        db_payment_type.name = payment_type_update.name
        db_payment_type.price = payment_type_update.price
        db.commit()
        db.refresh(db_payment_type)
    return db_payment_type
