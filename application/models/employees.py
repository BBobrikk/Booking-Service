from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from application.core.Connection import Base


class EmployeesORM(Base):
    __tablename__ = "Employees"

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    phone: Mapped[str]
    job_title: Mapped[str]
    salary: Mapped[int]

    __table_args__ = (
        CheckConstraint(
            "phone LIKE '+7__________' or phone LIKE '8__________'", "CHK_phone_valid"
        ),
        CheckConstraint("age BETWEEN 18 and 70", "CHK_age_valid"),
        CheckConstraint("salary > 0", "CHK_salary_valid"),
    )
