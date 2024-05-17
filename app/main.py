# -*- coding: utf-8 -*-
# app/main.py
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from sqlalchemy.orm import Session

from app.core.config import settings  # Importa la configuración
from app.db.base import Base
from app.db.session import SessionLocal, engine, get_db
#from app.init_data import create_sample_data
from app.routers import (grades, invoices, payment_types, payments, schools,
                         students, users)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mattilda API",
    description="API para gestionar colegios, estudiantes, facturas y pagos.",
    version="1.0.0",
    openapi_tags=[
        {"name": "schools",
            "description": "Operaciones relacionadas con la gestión de colegios"},
        {"name": "students",
            "description": "Operaciones relacionadas con la gestión de estudiantes"},
        {"name": "invoices",
            "description": "Operaciones relacionadas con la gestión de facturas"},
        {"name": "payments",
            "description": "Operaciones relacionadas con la gestión de pagos"},
        {"name": "payment_types",
            "description": "Operaciones relacionadas con la gestión de tipos de pago"},
        {"name": "grades", "description": "Operaciones relacionadas con la gestión de grados"},
        {"name": "users", "description": "Operaciones relacionadas con la gestión de usuarios"}
    ]
)

app.include_router(schools.router, prefix="/api", tags=["schools"])
app.include_router(students.router, prefix="/api", tags=["students"])
app.include_router(invoices.router, prefix="/api", tags=["invoices"])
app.include_router(payments.router, prefix="/api", tags=["payments"])
app.include_router(payment_types.router, prefix="/api", tags=["payment_types"])
app.include_router(grades.router, prefix="/api", tags=["grades"])
app.include_router(users.router, prefix="/api", tags=["users"])


# @app.on_event("startup")
# async def startup():
#     FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
#     if settings.ENVIRONMENT == "development":
#         db: Session = SessionLocal()
#         create_sample_data(db)
