import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="pingvinkrut"
)
cur = conn.cursor()

cur.execute("TRUNCATE TABLE phonebook")

conn.commit()
cur.close()
conn.close()
