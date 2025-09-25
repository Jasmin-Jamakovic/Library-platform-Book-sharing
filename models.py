from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, column,Float
from sqlalchemy.orm import relationship, sessionmaker, foreign
from sqlalchemy.ext.declarative import declarative_base
import datetime

DATABASE_URL = "postgresql://postgres:jasmin123@localhost:5432/BazaPodataka"
Base=declarative_base()

engine=create_engine(DATABASE_URL)


SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


class Book(Base):
    __tablename__="books"

    id=Column(Integer,primary_key=True,index=True)
    title =Column(String,index=True)
    author=Column(String)
    description=Column(String)
    available=Column(Boolean,default=True)
    created_at =Column(DateTime,default=datetime.datetime.utcnow)

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    email=Column(String,unique=True,index=True)

class Transaction(Base):
    __tablename__="Transactions"
    id=Column(Integer,primary_key=True,index=True)
    user_id=(Integer,ForeignKey("users.id"))
    book_id=(Integer,ForeignKey("book.id"))
    transaction_type=Column(String)
    amount=Column(Float)
    date=Column(DateTime,default=datetime.datetime.utcnow())

    user=relationship("User",back_populates="transactions")
    book=relationship("book",back_populates="transactions")


class Rental(Base):
    __tablename__="rentals"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    book_id=Column(Integer,ForeignKey("books.id"))
    start_date=Column(DateTime,default=datetime.datetime.utcnow())
    end_date=Column(DateTime,default=datetime.datetime.utcnow())
    status=Column(String,default="rented")

    user=relationship("User",back_populates="rentals")
    book=relationship("book",back_populates="rentals")


class Payment(Base):
    __tablename__="payments"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    amount=Column(Float)
    payment_date=Column(DateTime,default=datetime.datetime.utcnow())
    payment_status=Column(String)

    user=relationship("User",back_populates="payments")



Base.metadata.create_all(bind=engine)

