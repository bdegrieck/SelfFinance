from sqlalchemy import create_engine

url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(url)