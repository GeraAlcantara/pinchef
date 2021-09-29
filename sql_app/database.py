import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# read env variables
# load_dotenv()
# SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

SQLALCHEMY_DATABASE_URI = 'sqlite:///./pinchef.db'

# the argument is needed only for SQLite. It's not needed for other databases.
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False}) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()