import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="pingvinkrut"
)
cur = conn.cursor()

cur.execute("DROP TABLE user_score")
cur.execute("DROP TABLE users")

conn.commit()
cur.close()
conn.close()