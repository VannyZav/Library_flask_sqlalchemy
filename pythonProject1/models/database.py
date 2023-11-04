
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Genre(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    book: Mapped[str] = relationship("Book", back_populates="Genre")

    def __repr__(self):
        return f'Genre(name={self.name!r}'


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String)
    genre_id: Mapped[str] = mapped_column(String, ForeignKey(Genre.id, ondelete="SET NULL"))
    genre: Mapped[str] = relationship("Genre", back_populates="Book")

    def __repr__(self):
        return f'Book(name={self.name!r}'
    