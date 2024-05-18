from app.db.session import Base
from app.models import (
    Grade,
    Invoice,
    Payment,
    PaymentType,
    School,
    Student,
    User,
)

# Import all models to be included in Base
__all__ = [
    "Base",
    "User",
    "School",
    "Student",
    "Invoice",
    "Payment",
    "PaymentType",
    "Grade",
]
