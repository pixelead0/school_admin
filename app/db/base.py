# -*- coding: utf-8 -*-
from app.db.session import Base
from app.models.grade import Grade
from app.models.invoice import Invoice
from app.models.payment import Payment
from app.models.payment_type import PaymentType
from app.models.school import School
from app.models.student import Student
from app.models.user import User

# Import all models to be included in Base
__all__ = ["Base", "User", "School", "Student",
           "Invoice", "Payment", "PaymentType", "Grade"]
