from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DB_USER = "postgres"
DB_PASSWORD = "user"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

@app.get("/books")
def get_books():
  with engine.connect() as conn:
    result = conn.execute(text(
      "SELECT * FROM books LIMIT 50 "
      )).mappings()
    books = [dict(row) for row in result]
  return books


@app.get("/authors")
def get_authors():
  with engine.connect() as conn:
    result = conn.execute(text(
      "SELECT * FROM authors LIMIT 50 "
      )).mappings()
    authors = [dict(row) for row in result]
  return authors


@app.get("/books_with_details")
def get_books_with_details():
  with engine.connect() as conn:
    result = conn.execute(text(
      "SELECT b.*, a.name "
      "FROM books b "
      "INNER JOIN books_authors ba ON ba.book_id = b.book_id "
      "LEFT JOIN authors a ON ba.author_id = a.author_id "
      "LIMIT 50"
    )).mappings()
    books_with_details = [dict(row) for row in result]
  return books_with_details