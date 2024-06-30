from sqlalchemy import create_engine , Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()
query_data = Session()