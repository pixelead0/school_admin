from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.invoice import Invoice, InvoiceCreate
from app.crud.invoice import get_invoice, get_invoices, create_invoice, delete_invoice, update_invoice
from app.db.session import get_db
from typing import List
import uuid
import os

router = APIRouter()

@router.get("/invoices/", response_model=List[Invoice])
def read_invoices(skip: int = 0, limit: int = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10)), db: Session = Depends(get_db)):
    invoices = get_invoices(db, skip=skip, limit=limit)
    return invoices

@router.post("/invoices/", response_model=Invoice)
def create_invoice_endpoint(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db=db, invoice=invoice)

@router.get("/invoices/{invoice_id}", response_model=Invoice)
def read_invoice(invoice_id: uuid.UUID, db: Session = Depends(get_db)):
    db_invoice = get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

@router.delete("/invoices/{invoice_id}", response_model=Invoice)
def delete_invoice_endpoint(invoice_id: uuid.UUID, db: Session = Depends(get_db)):
    db_invoice = delete_invoice(db=db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

@router.put("/invoices/{invoice_id}", response_model=Invoice)
def update_invoice_endpoint(invoice_id: uuid.UUID, invoice: InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = update_invoice(db=db, invoice_id=invoice_id, invoice_update=invoice)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice
