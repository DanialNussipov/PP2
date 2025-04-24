import psycopg2
from tabulate import tabulate

def paginate(limit, offset):
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"
     )
     cur = conn.cursor()
     cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
     
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     cur.close()
     conn.close()
     
paginate(limit = 2, offset = 0)
paginate(limit = 2, offset = 2)
paginate(limit = 2, offset = 4)