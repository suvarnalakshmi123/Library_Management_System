from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "postgresql+psycopg2://postgres:ksl2003*@localhost/library_database"
engine = create_engine(URL)

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)