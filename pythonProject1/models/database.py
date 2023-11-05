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
    books = relationship("Book", back_populates="genre")

    def __repr__(self):
        return f'Genre(name={self.name!r})'


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String)
    genre_id: Mapped[int] = mapped_column(Integer, ForeignKey('genre.id', ondelete="SET NULL"))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f'Book(name={self.name!r})'





































#
# from typing import Type
#
# from sqlalchemy import Integer, String, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, relationship
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# db = SQLAlchemy(model_class=Base)
#
#
# class Book(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     author: Mapped[str] = mapped_column(String)
#     genre_id: Mapped[int] = mapped_column(Integer, ForeignKey('genre.id', ondelete="SET NULL"))
#     genre = relationship("Genre", back_populates="books")
#
#     def __repr__(self):
#         return f'Book(name={self.name!r})'
#
#
# class Genre(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String)
#     books = relationship("Book", back_populates="genre")
#
#     def __repr__(self):
#         return f'Genre(name={self.name!r})'





