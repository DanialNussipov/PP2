"""
Implement two ways of inserting data into the PhoneBook.
upload data from csv file
entering user name, phone from console
"""
import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(
     host = "localhost",
     dbname = "lab10",
     user = "postgres",
     password = "pingvinkrut"
)
cur = conn.cursor()

with open (r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab10\phonebook\phonebook.csv", 'r') as file:
     reader = csv.reader(file)
     next(reader)
     for row in reader:
          cur.execute("INSERT INTO phonebook (Surname, Name, Phone) VALUES (%s, %s, %s) ON CONFLICT (Phone) DO NOTHING", row)
               
Surname = input("Enter surname: ")
Name = input("Enter name: ")
Phone = input("Enter phone: ")

insert = ("INSERT INTO phonebook (Surname, Name, Phone) VALUES (%s, %s, %s) ON CONFLICT (Phone) DO NOTHING")
insert2 = (Surname, Name, Phone)
cur.execute(insert, insert2)

cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()
headers = ["ID", "Surname", "Name", "Phone"]
print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
conn.commit()
cur.close()
conn.close()