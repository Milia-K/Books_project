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

try:
  with engine.connect() as conn:
    print('✅ подключились к постгрескл')
except  SQLAlchemyError  as e:
  print('❌ не подключились', e)