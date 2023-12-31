from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DB_URL = "sqlite:///./db.sql"
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread":False})
DBSession = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()