import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="pingvinkrut"
)
cur = conn.cursor()

cur.execute(
     """ 
     CREATE TABLE IF NOT EXISTS users (
          user_id SERIAL PRIMARY KEY,
          username VARCHAR(50) NOT NULL
     )
     """)
cur.execute(
     """ 
     CREATE TABLE IF NOT EXISTS user_score (
          user_id INT REFERENCES users(user_id),
          score INT,
          level INT,
          coins_eaten INT DEFAULT 0,
          PRIMARY KEY (user_id)
     )
     """
)

conn.commit()
cur.close()
conn.close()