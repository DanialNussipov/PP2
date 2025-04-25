# Create function to querying data from the tables with pagination (by limit and offset)
import psycopg2
from tabulate import tabulate

def paginate():
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"
     )
     cur = conn.cursor()
     
     cur.execute("""
               CREATE OR REPLACE FUNCTION pagination(
                    p_limit INT,
                    p_offset INT
                    )
               RETURNS SETOF phonebook AS $$
               BEGIN
                    RETURN QUERY
                    SELECT * FROM phonebook
                    LIMIT p_limit OFFSET p_offset;
               END;
               $$ LANGUAGE plpgsql;                 
                 """)
     conn.commit()
     cur.close()
     conn.close()
     
def result(limit, offset):
     conn = psycopg2.connect(
          host = "localhost",
          dbname = "lab10",
          user = "postgres",
          password = "pingvinkrut"
     )
     cur = conn.cursor()
     cur.execute("SELECT * FROM pagination(%s, %s)", (limit, offset))
     rows = cur.fetchall()
     headers = ["ID", "Surname", "Name", "Phone"]
     print(tabulate(rows, headers = headers, tablefmt = "pretty"))
     
     conn.commit()
     cur.close()
     conn.close()
     
paginate()
result(2, 0)
result(3, 1)
result(2, 1)
