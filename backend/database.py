from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:123gr@localhost:4321/task_app')

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

