from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime


class UserCreate(BaseModel):
    name:str
    email:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

    class config:
        orm_mode=True


class BookBase(BaseModel):
    title:str
    author:str
    description:Optional[str]=None
    available=Optional[bool]=True

class BookResponse(BookBase):
    id:int
    created_at:datetime

    class Config:
        orm_mode=True

class TransactionBase(BaseModel):
    transaction_type:str
    amount:float


class TransactionCreate(BaseModel):
    user_id:int
    book_id=int

class TransactionResponse(BaseModel):
    id:int
    user_id=int
    book_id=int
    date:datetime

    class config:
        orm_mode=True


class RentalBase(BaseModel):
    start_date=datetime
    end_date=datetime
    status:Optional[str]="rented"

class RentalCreate(BaseModel):
    user_id=int
    book_id=int


class RentalResponse(BaseModel):
    id:int
    user_id:int
    book_id:int

    class Config:
        orm_mode=True


class PaymentBase(BaseModel):
    amount:float
    payment_status:str


class PaymentCreate(BaseModel):
    id:int
    user_id=int
    payment_date=datetime

    class Config:
        orm_mode=True