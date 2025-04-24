# Implement deleting data from tables by username of phone
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

name = input("Enter name whos information you want to delete: ")
surname = input("Enter surname whos information you want to delete: ")

cur.execute("SELECT * FROM phonebook WHERE name = %s AND surname = %s", (name, surname))
user = cur.fetchone()

if user:
     cur.execute("DELETE FROM phonebook WHERE name = %s AND surname = %s", (name, surname))
     print("--- Phonebook ---")
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     for row in rows:
          print(row)
     print("Information deleted successfully!")
else:
     print("There is no user with this name/surname")

conn.commit()
cur.close()
conn.close()   