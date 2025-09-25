from http.client import HTTPException

from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import models
from pydantic import BaseModel
from database import get_db



app=FastAPI()

from models import User
class UserCreate(BaseModel):
    name:str
    email:str

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already taken
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




@app.get("/")
def root():
    return {"Message":"Poruka"}

@app.get("/users/{user_id}")
def get_user(user_id: int,db: Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user
