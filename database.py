from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import models

engine = create_engine("sqlite:///vacancies.db", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)