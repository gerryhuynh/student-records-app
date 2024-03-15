import psycopg

try:
    conn = psycopg.connect(
        "dbname='students' user='postgres' host='localhost' password='student1'"
    )
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
