# app/main.py
from fastapi import Depends, FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.dependencies import get_current_user
from app.core.logging_config import logger
from app.db.base import Base
from app.db.session import SessionLocal, engine, get_db
from app.routers import (
    grades,
    invoices,
    payment_types,
    payments,
    schools,
    students,
    users,
)

# from app.init_data import create_sample_data

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="School Admin",
    description="API para gestionar colegios, estudiantes, facturas y pagos.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "schools",
            "description": "Operaciones relacionadas con la gestión de colegios",
        },
        {
            "name": "students",
            "description": "Operaciones relacionadas con la gestión de estudiantes",
        },
        {
            "name": "invoices",
            "description": "Operaciones relacionadas con la gestión de facturas",
        },
        {
            "name": "payments",
            "description": "Operaciones relacionadas con la gestión de pagos",
        },
        {
            "name": "payment_types",
            "description": "Operaciones relacionadas con la gestión de tipos de pago",
        },
        {
            "name": "grades",
            "description": "Operaciones relacionadas con la gestión de grados",
        },
        {
            "name": "users",
            "description": "Operaciones relacionadas con la gestión de usuarios",
        },
    ],
)

app.include_router(
    schools.router,
    prefix="/api",
    tags=["schools"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    students.router,
    prefix="/api",
    tags=["students"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    invoices.router,
    prefix="/api",
    tags=["invoices"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    payments.router,
    prefix="/api",
    tags=["payments"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    payment_types.router,
    prefix="/api",
    tags=["payment_types"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    grades.router,
    prefix="/api",
    tags=["grades"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(users.router, prefix="/api", tags=["users"])


@app.on_event("startup")
def startup_event():
    logger.info("Application startup")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("Application shutdown")


# @app.on_event("startup")
# async def startup():
#     FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
#     if settings.ENVIRONMENT == "development":
#         db: Session = SessionLocal()
#         create_sample_data(db)
