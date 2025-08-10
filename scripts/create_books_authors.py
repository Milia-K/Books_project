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
books_df = pd.read_sql('books', engine)
authors_df = pd.read_sql('authors', engine)

books_raw_df['author_list'] = books_raw_df['authors'].str.split(',').apply(lambda x: [a.strip() for a in x])

books_authors = []

for _, row in books_raw_df.iterrows():
  book_row = books_df[books_df['title'] == row['title']]
  if book_row.empty:
    continue
  book_id = book_row.iloc[0]['book_id']

  for author_name in row['author_list']:
    author_row = authors_df[authors_df['name'] == author_name]
    if author_row.empty:
      continue
    author_id = author_row.iloc[0]['author_id']
    books_authors.append({'book_id': book_id, 'author_id': author_id})

books_authors_df = pd.DataFrame(books_authors)

books_authors_df.to_sql('books_authors', engine, if_exists='append', index=False)

print('все вышло')
