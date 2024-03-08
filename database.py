from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_db="sqlite:///./allorders.db"

engine = create_engine(sqlalchemy_db, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    datab=SessionLocal()
    try:
        yield datab
    finally:
        datab.close()