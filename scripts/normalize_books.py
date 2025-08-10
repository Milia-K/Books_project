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
needed_columns = [
  'book_id', 'title', 'original_title', 'original_publication_year', 
  'language_code', 'average_rating', 'ratings_count', 'image_url'
]
books_df_filtered = books_raw_df[needed_columns]

try:
  books_df_filtered.to_sql('books', engine, if_exists='append', index= False)
except Exception as e:
  print("❌ Произошла ошибка:", e)