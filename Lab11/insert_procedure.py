import psycopg2
from tabulate import tabulate

def update():
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"
     )

     cur = conn.cursor()
     cur.execute(
     """
     CREATE OR REPLACE PROCEDURE InsertOrUpdate(
          p_surname TEXT,
          p_name TEXT,
          p_phone TEXT
     )
     LANGUAGE plpgsql
     AS $$
     BEGIN
          IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
               UPDATE phonebook SET phone = p_phone WHERE name = p_name OR surname = p_surname;
          ELSE
               INSERT INTO phonebook (surname, name, phone) VALUES (p_surname, p_name, p_phone);
          END IF;
     END;
     $$;
     """
     )
     
     print("--- Phonebook ---")
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     conn.commit()
     cur.close()
     conn.close()
     
def InsertOrUpdate(surname, name, phone):
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"           
     )
     cur = conn.cursor()
     cur.execute("CALL InsertOrUpdate(%s, %s, %s);", (surname, name, phone))
    
     print("--- Phonebook ---")
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     conn.commit()
     cur.close()
     conn.close()
     
update()
InsertOrUpdate("Ospanov", "Dimash", "99988877743")
InsertOrUpdate("John", "Doe", "12312312312")