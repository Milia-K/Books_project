import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError 

DB_USER = "postgres"
DB_PASSWORD = "user"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
csv_path = '../data/books.csv'

try:
  df = pd.read_csv(csv_path)
  print('прочитано')
  df.to_sql('books', con=engine, if_exists='replace', index=False)
  print("Данные успешно загружены в таблицу 'books'")

except FileNotFoundError:
  print("CSV-файл не найден по пути:", csv_path)
except Exception as e:
  print("Произошла другая ошибка:", e)
except  SQLAlchemyError  as e:
  print("Ошибка подключения", e)