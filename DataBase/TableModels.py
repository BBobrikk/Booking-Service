from datetime import date
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Connection import Base


class UsersORM(Base):

    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone: Mapped[str]
    mail: Mapped[str]
    rooms : Mapped[list["RoomsORM"]] = relationship(back_populates = "user")

    __table_args__ = (
            CheckConstraint(
                "phone LIKE +7__________ or phone LIKE 8__________", "CHK_user_phone_valid"),
            CheckConstraint(
                "mail LIKE %@gmail.com or mail LIKE %@mail.ru", "CHK_mail_valid"),
        )


class RoomsORM(Base):

    __tablename__ = "Rooms"

    room_id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    grade: Mapped[int]
    beds: Mapped[int]
    booking_start: Mapped[date]
    booking_end: Mapped[date]
    user_id : Mapped[int] = mapped_column(ForeignKey(UsersORM.user_id))
    user : Mapped[UsersORM] = relationship(back_populates = "rooms")

    __table_args__ = (
          CheckConstraint(
            "grade in ('standard', 'luxe', 'president')", "CHK_grade_valid"),
          CheckConstraint(
                  "booking_start <= booking_end,", "CHK_date_valid")
        )

class EmployeesORM(Base):

     __tablename__ = "Employees"

     employee_id : Mapped[int] = mapped_column(primary_key=True)
     name : Mapped[str]
     age : Mapped[int]
     phone : Mapped[str]
     job_title : Mapped[str]
     salary : Mapped[int]

     __table_args__ = (
          CheckConstraint(
               "phone LIKE +7__________ or phone LIKE 8__________", "CHK_phone_valid"),
          CheckConstraint(
               "age BETWEEN 18 and 70", "CHK_age_valid"),
          CheckConstraint(
          "salary > 0", "CHK_salary_valid")
     )