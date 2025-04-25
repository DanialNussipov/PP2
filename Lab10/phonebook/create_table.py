import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="pingvinkrut"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        Surname VARCHAR(100) NOT NULL,
        Name VARCHAR(100) NOT NULL,
        Phone VARCHAR(20) UNIQUE NOT NULL
    )
""")

conn.commit()
cur.close()
conn.close()
