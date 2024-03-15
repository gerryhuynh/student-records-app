import psycopg

# PostgresSQL DB connection settings
DB_NAME = "students"
USER = "postgres"
HOST = "localhost"
PASSWORD = "student1"

"""
getAllStudents(): Retrieves and displays all records from the students table.
addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
deleteStudent(student_id): Deletes the record of the student with the specified student_id.
"""


# Establishes connection to the students database
# Returns a connection object
def connect():
    # connect to the students database
    try:
        conn = psycopg.connect(
            f"dbname={DB_NAME} user={USER} host={HOST} password={PASSWORD}"
        )
    # if the connection fails, print the error and exit
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
        exit(1)
    # return the connection object
    return conn


# Retrieves and displays all records from the students table
# Returns nothing
def getAllStudents():
    conn = connect()
    with conn.cursor() as cursor:
        # query the students table
        cursor.execute("SELECT * FROM students")
        # fetch all the rows
        rows = cursor.fetchall()
        # print all the rows
        for row in rows:
            print(row)
    conn.close()


if __name__ == "__main__":
    getAllStudents()
