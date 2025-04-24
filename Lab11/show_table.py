import psycopg2
from tabulate import tabulate

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
headers = ["ID", "Surname", "Name", "Phone"]
print(tabulate(rows, headers = headers, tablefmt = "pretty"))
    

conn.commit()
cur.close()
conn.close()
