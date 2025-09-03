import psycopg

try:
    conn = psycopg.connect(
        dbname="fastapi",
        user="postgres",
        password="12345",  # replace with your postgres password
        host="127.0.0.1",
        port=5433
    )
    print("Connected to PostgreSQL successfully!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
