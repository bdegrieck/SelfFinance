from sqlalchemy import create_engine
import os

def start_engine():
    username = os.getenv("POSTGRES_USERNAME")
    password = os.getenv("POSTGRES_PASSWORD")
    url = f"postgresql+psycopg2://{username}:{password}@localhost:5432/local"
    engine = create_engine(url)
    return engine