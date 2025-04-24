import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="pingvinkrut"
)
cur = conn.cursor()

print("--- Phonebook ---")
cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()
for row in rows:
    print(row)
    

conn.commit()
cur.close()
conn.close()
