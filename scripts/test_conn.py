import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="user",
        host="localhost",
        port="5432"
    )
    print("✅ Подключение успешно!")
    conn.close()
except Exception as e:
        print(f"❌ Ошибка подключения: {repr(e)}")
