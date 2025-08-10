import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "user"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

books_raw_df = pd.read_sql('books_raw', engine)
authors_series = books_raw_df['authors'].str.split(',').explode().str.strip()
unique_authors = authors_series.drop_duplicates().reset_index(drop=True)

authors_df = pd.DataFrame({'name': unique_authors})

try:
  authors_df.to_sql('authors', engine, if_exists='append', index=False)
except Exception as e:
  print("❌ Произошла ошибка:", e)