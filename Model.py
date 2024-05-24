from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float, Text
from sqlalchemy.orm import declarative_base
from decimal import Decimal
from sqlalchemy.orm import sessionmaker


URL ="postgresql+psycopg2://postgres:ksl2003*@localhost/library_database"

engine = create_engine(URL)

Base = declarative_base()
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    last_login = Column(DateTime)
    role = Column(String, nullable=False)

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    ISBN = Column(Integer, unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    inventory = Column(Integer, nullable=False)
    borrowed_books = Column(Integer, nullable=True)
    return_books =  Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    renew_a_book = Column(Boolean, nullable=False)
    fine_amount = Column(Float, nullable=True)
    price_of_the_book = Column(Float, nullable=False)
    

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()