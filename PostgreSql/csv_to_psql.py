import psycopg2
import csv

# Connect to PostgeSQL
conn = psycopg2.connect(
     host = "localhost",
     dbname = "mydatabase",
     user = "postgres",
     password = "pingvinkrut"
)
cur = conn.cursor()

# Open the CSV file
with open (r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\PostgreSql\names.csv", 'r') as file:
     reader = csv.reader(file)
     next(reader)
     for row in reader:
          cur.execute("INSERT INTO musicians (singer, band, song) VALUES (%s, %s, %s)", row)
               
singer = input("Enter singer: ")
band = input("Enter band: ")
song = input("Enter song: ")

insert = ("INSERT INTO musicians (singer, band, song) VALUES (%s, %s, %s)")
insert2 = (singer, band, song)
cur.execute(insert, insert2)
     
conn.commit()
cur.close()
conn.close()