from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from application.core.connection import Base


class UsersORM(Base):

    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str]
    mail: Mapped[str]
    bookings: Mapped[list["BookingsORM"]] = relationship(back_populates="user")

    # __table_args__ = (
    #     CheckConstraint(
    #         "phone LIKE '+7__________' or phone LIKE '8__________'",
    #         "CHK_user_phone_valid",
    #     ),
    #     CheckConstraint(
    #         "mail LIKE '%@gmail.com' or mail LIKE '%@mail.ru'", "CHK_mail_valid"
    #     ),
    # )
