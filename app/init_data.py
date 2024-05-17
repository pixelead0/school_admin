import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.school import School
from app.models.student import Student
from app.models.grade import Grade
from app.models.payment_type import PaymentType
from app.models.payment import Payment
from app.models.invoice import Invoice
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_sample_data(db: Session):
    # Crear colegios
    school1 = School(
        id=uuid.uuid4(),
        name="Colegio Nacional",
        country="Mexico",
        state="CDMX",
        description="Colegio de alta calidad",
        period_type="bimestral"
    )
    school2 = School(
        id=uuid.uuid4(),
        name="Instituto Moderno",
        country="Mexico",
        state="Guadalajara",
        description="Instituto moderno y tecnológico",
        period_type="trimestral"
    )
    db.add(school1)
    db.add(school2)
    db.commit()

    # Crear usuarios vinculados a colegios
    user1 = User(
        id=uuid.uuid4(),
        username="admin_colegio_nacional",
        hashed_password=pwd_context.hash("password"),
        school_id=school1.id
    )
    user2 = User(
        id=uuid.uuid4(),
        username="admin_instituto_moderno",
        hashed_password=pwd_context.hash("password"),
        school_id=school2.id
    )
    db.add(user1)
    db.add(user2)
    db.commit()

    # Crear grados
    grade1 = Grade(
        id=uuid.uuid4(),
        name="1st Grade",
        school_id=school1.id
    )
    grade2 = Grade(
        id=uuid.uuid4(),
        name="2nd Grade",
        school_id=school1.id
    )
    grade3 = Grade(
        id=uuid.uuid4(),
        name="1st Grade",
        school_id=school2.id
    )
    db.add(grade1)
    db.add(grade2)
    db.add(grade3)
    db.commit()

    # Crear estudiantes vinculados a colegios y grados
    student1 = Student(
        id=uuid.uuid4(),
        first_name="Juan",
        last_name_father="Perez",
        last_name_mother="Gomez",
        enrollment="12345",
        grade_id=grade1.id,
        school_id=school1.id
    )
    student2 = Student(
        id=uuid.uuid4(),
        first_name="Maria",
        last_name_father="Lopez",
        last_name_mother="Diaz",
        enrollment="67890",
        grade_id=grade2.id,
        school_id=school1.id
    )
    student3 = Student(
        id=uuid.uuid4(),
        first_name="Carlos",
        last_name_father="Hernandez",
        last_name_mother="Martinez",
        enrollment="54321",
        grade_id=grade3.id,
        school_id=school2.id
    )
    db.add(student1)
    db.add(student2)
    db.add(student3)
    db.commit()

    # Crear tipos de pago
    payment_type1 = PaymentType(
        id=uuid.uuid4(),
        name="Tuition",
        price=1000.0
    )
    payment_type2 = PaymentType(
        id=uuid.uuid4(),
        name="Library Fee",
        price=100.0
    )
    db.add(payment_type1)
    db.add(payment_type2)
    db.commit()

    # Crear pagos
    payment1 = Payment(
        id=uuid.uuid4(),
        student_id=student1.id,
        school_id=school1.id,
        payment_type_id=payment_type1.id
    )
    payment2 = Payment(
        id=uuid.uuid4(),
        student_id=student2.id,
        school_id=school1.id,
        payment_type_id=payment_type2.id
    )
    payment3 = Payment(
        id=uuid.uuid4(),
        student_id=student3.id,
        school_id=school2.id,
        payment_type_id=payment_type1.id
    )
    db.add(payment1)
    db.add(payment2)
    db.add(payment3)
    db.commit()

    # Crear facturas
    invoice1 = Invoice(
        id=uuid.uuid4(),
        student_id=student1.id,
        amount=1000.0,
        payment_id=payment1.id,
        date="2024-01-01"
    )
    invoice2 = Invoice(
        id=uuid.uuid4(),
        student_id=student2.id,
        amount=100.0,
        payment_id=payment2.id,
        date="2024-01-02"
    )
    invoice3 = Invoice(
        id=uuid.uuid4(),
        student_id=student3.id,
        amount=1000.0,
        payment_id=payment3.id,
        date="2024-01-03"
    )
    db.add(invoice1)
    db.add(invoice2)
    db.add(invoice3)
    db.commit()
