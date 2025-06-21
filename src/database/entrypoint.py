import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema="Sales")
Base = declarative_base(metadata=metadata)
load_dotenv()


def create_test_db():
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/Finance"
    engine = create_engine(url, echo=False)
    with engine.begin() as conn:
        conn.execute(text('CREATE SCHEMA IF NOT EXISTS "Sales"'))
        Base.metadata.create_all(bind=conn)
    return engine


def create_db():
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/Finance"
    engine = create_engine(url, echo=False)
    with engine.begin() as conn:
        conn.execute(text('CREATE SCHEMA IF NOT EXISTS "dbo"'))
        Base.metadata.create_all(bind=conn)
    return engine
