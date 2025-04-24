import psycopg2
from tabulate import tabulate

def procedure():
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"
     )
     
     cur = conn.cursor()
     
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     cur.execute(
     """
     CREATE OR REPLACE PROCEDURE DeleteByNameOrPhone(
          p_name TEXT,
          p_phone TEXT
     )
     LANGUAGE plpgsql
     AS $$
     BEGIN
          DELETE FROM phonebook
          WHERE name = p_name OR phone = p_phone;
     END;
     $$;
     """
     )
     conn.commit()
     cur.close()
     conn.close()

def delete(name, phone):
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"
     )
     
     cur = conn.cursor()
     cur.execute("CALL DeleteByNameOrPhone(%s, %s)", (name, phone))
     
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     conn.commit()
     cur.close()
     conn.close()

procedure()
name = input("Enter name: ")
phone = input("Enter phone: ")
delete(name, phone)