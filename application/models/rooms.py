from datetime import date
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from application.core.Connection import Base
from application.models.users import UsersORM


class RoomsORM(Base):

    __tablename__ = "Rooms"

    room_id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    grade: Mapped[str]
    beds: Mapped[int]
    booking_start: Mapped[date]
    booking_end: Mapped[date]
    user_id : Mapped[int] = mapped_column(ForeignKey(UsersORM.user_id))
    user : Mapped["UsersORM"] = relationship(back_populates = "rooms")

    __table_args__ = (
          CheckConstraint(
            "grade in ('standard', 'luxe', 'president')", "CHK_grade_valid"),
          CheckConstraint(
                  "booking_start <= booking_end", "CHK_date_valid")
        )