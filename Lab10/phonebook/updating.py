"""
Implement updating data in the table (change user first name or phone)
"""
import psycopg2

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
for row in rows:
    print(row)
    
surname_to_update = input("Enter surname whos info you want to change: ")

cur.execute("SELECT * FROM phonebook WHERE surname = %s", (surname_to_update,))
user = cur.fetchone()


if user:
     print("What do you want to change?")
     print("1.name")
     print("2.phone")

     action = int(input("Your choice: "))
     if action == 1:
          new_name = input("Enter new name: ")
          cur.execute("""
                    UPDATE phonebook
                    SET name = %s
                    WHERE surname = %s;
                    """, (new_name, surname_to_update))
     elif action == 2:
          new_phone = input("Enter new phone: ")
          cur.execute("""
                    UPDATE phonebook
                    SET phone = %s
                    WHERE surname = %s;
                    """, (new_phone, surname_to_update))
     else:
          print("Wrong action!")
else:
     print("there is no user person with this surname!")
     
if user:
     print("--- Phonebook ---")
     cur.execute("SELECT * FROM phonebook")
     rows = cur.fetchall()
     for row in rows:
          print(row)
     print("Information changed successfully!")

    

conn.commit()
cur.close()
conn.close()