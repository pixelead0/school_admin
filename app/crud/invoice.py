import os
import uuid

from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate

PAGINATION_DEFAULT_LIMIT = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10))


def get_invoice(db: Session, invoice_id: uuid.UUID):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()


def get_invoices(db: Session, skip: int = 0, limit: int = PAGINATION_DEFAULT_LIMIT):
    return db.query(Invoice).offset(skip).limit(limit).all()


def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoice(
        id=uuid.uuid4(),
        student_id=invoice.student_id,
        amount=invoice.amount,
        payment_id=invoice.payment_id,
        date=invoice.date,
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def delete_invoice(db: Session, invoice_id: uuid.UUID):
    db_invoice = get_invoice(db, invoice_id)
    if db_invoice:
        db.delete(db_invoice)
        db.commit()
    return db_invoice


def update_invoice(db: Session, invoice_id: uuid.UUID, invoice_update: InvoiceCreate):
    db_invoice = get_invoice(db, invoice_id)
    if db_invoice:
        db_invoice.student_id = invoice_update.student_id
        db_invoice.amount = invoice_update.amount
        db_invoice.payment_id = invoice_update.payment_id
        db_invoice.date = invoice_update.date
        db.commit()
        db.refresh(db_invoice)
    return db_invoice
