# Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
import psycopg2
from tabulate import tabulate

def pattern():
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"    
     )
     
     cur = conn.cursor()
     
     print("--- Phonebook ---")
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     pattern_input = input(("Enter part from name or surname or phone: "))
     pattern = f"%{pattern_input}%"
     cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s", (pattern, pattern, pattern))

     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     if rows:
          print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     else:
          print("Have not found anything")

     cur.close()
     conn.close()               

pattern()