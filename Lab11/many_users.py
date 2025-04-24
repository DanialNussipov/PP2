import psycopg2
from tabulate import tabulate

def many_users():
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = 'postgres',
          password = "pingvinkrut"
     )
     
     cur = conn.cursor()
     cur.execute(
     """
     CREATE OR REPLACE FUNCTION ManyUsers(
          surnames TEXT[],
          names TEXT[],
          phones TEXT[]
     ) RETURNS TEXT[] AS $$
     DECLARE
          invalid TEXT[] := '{}';
          i INT := 1;
     BEGIN
          WHILE i <= array_length(names, 1) LOOP
               IF length(phones[i]) = 5 AND phones[i] ~ '^\\d+$' THEN
                    INSERT INTO phonebook(surname, name, phone) VALUES (surnames[i], names[i], phones[i]);
               ELSE
                    invalid := array_append(invalid, surnames[i] || ' ' || names[i] || ' ' || phones[i]);
               END IF;
               i := i + 1;
          END LOOP;
          RETURN invalid;
     END;
     $$ LANGUAGE plpgsql;
     """
     )
     conn.commit()
     cur.close()
     conn.close()
     
def users(surnames, names, phones):
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = 'postgres',
          password = "pingvinkrut"
     )
     
     cur = conn.cursor()
     cur.execute("SELECT ManyUsers(%s, %s, %s)", (surnames, names, phones))
     invalid = cur.fetchone()
     
     if invalid:
          print("invalid data:")
          for row in invalid:
               print(row)
     else:
          print("Users Inserted Successfully!")
          
     conn.commit()
     cur.close()
     conn.close()
     
many_users()
surnames = ["Wayne", "Bennington", "Bone"]
names = ["Bruce", "Chester", "Papyrus"]
phones = ["11111", "78787", "777a7"]
users(surnames, names, phones)
     