from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class db_user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    borrowing_user = relationship('db_borrowing', back_populates='user')


class db_book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(Integer, unique=True)
    borrowed_until = Column(Date)
    borrowed_book = relationship('db_borrowing', back_populates='book')


class db_borrowing(Base):
    __tablename__ = 'borrowings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    start = Column(Date)
    end = Column(Date)
    book = relationship('db_book', back_populates='borrowed_book')
    user = relationship('db_user', back_populates='borrowing_user')
