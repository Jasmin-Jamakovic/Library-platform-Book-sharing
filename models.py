from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, column
from sqlalchemy.orm import relationship,sessionmaker
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


Base.metadata.create_all(bind=engine)

