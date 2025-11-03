from datetime import date
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from application.core.connection import Base


class BookingsORM(Base):

    __tablename__ = "Bookings"

    booking_id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    price: Mapped[int]
    wishes: Mapped[str]
    start_date: Mapped[date]
    end_date: Mapped[date]
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))
    room_id: Mapped[int] = mapped_column(ForeignKey("Rooms.room_id"))
    user: Mapped["UsersORM"] = relationship(back_populates="bookings")
    room: Mapped["RoomsORM"] = relationship(back_populates="bookings")

    # __table_args__ = (
    #     CheckConstraint("start_date <= end_date", "CHK_date_valid"),
    #     CheckConstraint("price > 0", "CHK_price_valid"),
    # )
