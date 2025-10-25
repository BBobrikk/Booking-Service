from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from application.core.connection import Base


class RoomsORM(Base):

    __tablename__ = "Rooms"

    room_id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    grade: Mapped[str]
    beds: Mapped[int]
    bookings: Mapped[list["BookingsORM"]] = relationship(back_populates="room")

    __table_args__ = (
        CheckConstraint(
            "grade in ('standard', 'luxe', 'president')", "CHK_grade_valid"
        ),
    )
