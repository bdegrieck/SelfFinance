import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def get_engine():
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/local"
    engine = create_engine(url)
    Base.metadata.create_all()
    return engine
