from sqlalchemy import ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(40))
    hashed_password: Mapped[str] = mapped_column(String())

    token: Mapped['Token'] = relationship(back_populates='parent')

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.username!r})'


class Token(Base):
    __tablename__ = 'tokens'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        server_default=text('uuid_generate_v4()'),
        unique=True,
        nullable=False,
        index=True
    )
    expires = mapped_column(DateTime())
    user_id = mapped_column(ForeignKey('users.id'))

    user: Mapped['User'] = relationship(back_populates='children',
                                        single_parent=True)
