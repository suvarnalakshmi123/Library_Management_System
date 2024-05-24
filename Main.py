from fastapi import FastAPI, Depends
from typing import Annotated
from pydantic import BaseModel
from Database import engine, SessionLocal
from sqlalchemy.orm import Session
from Database import Base

Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



db_dependency = Annotated[Session, Depends(get_db)]