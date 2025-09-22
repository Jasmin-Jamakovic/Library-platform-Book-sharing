from fastapi import FastAPI
from sqlalchemy.orm import Session
import models
from pydantic import BaseModel



app=FastAPI()

@app.get("/")
def root():
    return {"Message":"Poruka"}