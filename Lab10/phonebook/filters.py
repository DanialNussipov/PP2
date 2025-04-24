# Querying data from the tables (with different filters)
import psycopg2

conn = psycopg2.connect(
     host = "localhost",
     dbname = "lab10",
     user = "postgres",
     password = "pingvinkrut"
)
cur = conn.cursor()
done = False
          
print("--- Phonebook ---")
cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()
for row in rows:
    print(row)
              
print("How you want to sort table?:")
print("1.In ascending order")
print("2.in descending order")
action = int(input("Your choice?: "))

if action == 1:
     print("By what?: ")
     print("1.Name")
     print("2.Surname")
     print("3.Phone")
     action2 = int(input("Your choice?: "))
     if action2 == 1:
          cur.execute("SELECT * FROM phonebook ORDER BY name ASC ")
          done = True
     elif action2 == 2:
          cur.execute("SELECT * FROM phonebook ORDER BY surname ASC ")
          done = True
     elif action2 == 3:
          cur.execute("SELECT * FROM phonebook ORDER BY phone ASC ")
          done = True
     else:
          print("Wrong action!")
if action == 2:
     print("By what?: ")
     print("1.Name")
     print("2.Surname")
     print("3.Phone")
     action2 = int(input("Your choice?: "))
     if action2 == 1:
          cur.execute("SELECT * FROM phonebook ORDER BY name DESC ")
          done = True
     elif action2 == 2:
          cur.execute("SELECT * FROM phonebook ORDER BY surname DESC ")
          done = True
     elif action2 == 3:
          cur.execute("SELECT * FROM phonebook ORDER BY phone DESC ")
          done = True
     else:
          print("Wrong action!")

if done:
     print("--- Phonebook ---")
     rows = cur.fetchall()
     for row in rows:
          print(row)
     print("Information filtered")
else:
     print("Something went wrong:(")

conn.commit()
cur.close()
conn.close()