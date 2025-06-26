import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import declarative_base

load_dotenv()
metadata = MetaData()
Base = declarative_base(metadata=metadata)


def create_db():
    schema = "dbo"
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/Finance"
    engine = create_engine(url, echo=False)
    with engine.begin() as conn:
        conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))
        conn.execute(text(f'SET search_path TO "{schema}"'))
        metadata.schema = schema
        Base.metadata.create_all(bind=conn)
        metadata.schema = None  # reset back
    return engine


def create_test_database():
    schema = "test"
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/Test"
    engine = create_engine(url, echo=False)
    with engine.begin() as conn:
        conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))
        conn.execute(text(f'SET search_path TO "{schema}"'))
        metadata.schema = schema
        Base.metadata.drop_all(bind=conn)
        Base.metadata.create_all(bind=conn)
        metadata.schema = None  # reset back
    return engine


def clear_database():
    """Drop all tables in the Finance database."""
    schema = "dbo"
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/Finance"
    engine = create_engine(url, echo=False)
    with engine.begin() as conn:
        conn.execute(text(f'SET search_path TO "{schema}"'))
        metadata.schema = schema
        Base.metadata.drop_all(bind=conn)
        metadata.schema = None
    return engine
