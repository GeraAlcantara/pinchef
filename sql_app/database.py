from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'sqlite:///./sql_app.db'

# the argument is needed only for SQLite. It's not needed for other databases.
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False}) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()