import os

try:  # python-dotenv may not be available in minimal test environments
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover - fallback for missing optional dependency
    def load_dotenv(*args, **kwargs):
        """Fallback ``load_dotenv`` when python-dotenv isn't installed."""
        return False
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
        conn.execute(text('CREATE SCHEMA IF NOT EXISTS "Test"'))
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
