CREATE TABLE authors (
  author_id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE books (
  book_id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  original_title TEXT,
  original_publication_year INT,
  language_code TEXT,
  average_rating NUMERIC(3,2) NOT NULL,
  ratings_count INT,
  image_url TEXT
);

CREATE TABLE book_authors (
  book_id INT REFERENCES books(book_id) ON DELETE CASCADE,
  author_id INT REFERENCES authors(author_id) ON DELETE CASCADE,
  PRIMARY KEY (book_id, author_id)
);

CREATE TABLE book_genre (
  book_id INT REFERENCES books(book_id) ON DELETE CASCADE,
  genre_id INT REFERENCES genres(genre_id) ON DELETE CASCADE,
  PRIMARY KEY (book_id, author_id)
);

CREATE TABLE ratings_breakdown (
    book_id INT PRIMARY KEY REFERENCES books(book_id),
    ratings_1 INT,
    ratings_2 INT,
    ratings_3 INT,
    ratings_4 INT,
    ratings_5 INT
);
