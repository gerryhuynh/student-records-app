import psycopg

# PostgresSQL DB connection settings
DB_NAME = "students"
USER = "postgres"
HOST = "localhost"
PASSWORD = "student1"


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
        print(f"Connection Operational Error: {e}")
        exit(1)
    # return the connection object
    return conn


# Retrieves and displays all records from the students table
# Returns nothing
def getAllStudents():
    conn = None
    try:
        conn = connect()
        with conn.cursor() as cursor:
            # query the students table
            cursor.execute("SELECT * FROM students")
            # fetch all the rows
            rows = cursor.fetchall()
            # print all the rows
            for row in rows:
                print(row)
    # if the query fails, print the error
    except psycopg.DatabaseError as e:
        print(f"Database Error: {e}")
    # close the connection
    finally:
        if conn:
            conn.close()


# Inserts a new student record into the students table
# Returns nothing
def addStudent(first_name, last_name, email, enrollment_date):
    conn = None
    try:
        conn = connect()
        with conn.cursor() as cursor:
            # insert a new record into the students table
            cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date),
            )
            print(f"Added {first_name} {last_name} to the students table")
            conn.commit()
    # if the insertion fails, print the error
    except psycopg.DatabaseError as e:
        print(f"Database Error: {e}")
    # close the connection
    finally:
        if conn:
            conn.close()


# Updates the email address for a student with the specified student_id
# Returns nothing
def updateStudentEmail(student_id, new_email):
    conn = None
    try:
        conn = connect()
        with conn.cursor() as cursor:
            # update the email address for the specified student_id
            cursor.execute(
                f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id}"
            )
            print(f"Updated email for student {student_id} to {new_email}")
            conn.commit()
    # if the update fails, print the error
    except psycopg.DatabaseError as e:
        print(f"Database Error: {e}")
    # close the connection
    finally:
        if conn:
            conn.close()


# Deletes the record of the student with the specified student_id
# Returns nothing
def deleteStudent(student_id):
    conn = None
    try:
        conn = connect()
        with conn.cursor() as cursor:
            # delete the record for the specified student_id
            cursor.execute(f"DELETE FROM students WHERE student_id = {student_id}")
            print(f"Deleted student {student_id}")
            conn.commit()
    # if the deletion fails, print the error
    except psycopg.DatabaseError as e:
        print(f"Database Error: {e}")
    # close the connection
    finally:
        if conn:
            conn.close()


# Main function
# Calls the getAllStudents, addStudent, updateStudentEmail, and deleteStudent functions
if __name__ == "__main__":
    print("ALL STUDENTS:")
    getAllStudents()

    print("\nADDING A NEW STUDENT...")
    addStudent("John", "Smith", "john.smith@example.com", "2023-09-03")

    print("\nUPDATED ALL STUDENTS:")
    getAllStudents()

    print("\nUPDATING STUDENT 4'S EMAIL...")
    updateStudentEmail(4, "new.email@example.com")

    print("\nUPDATED ALL STUDENTS:")
    getAllStudents()

    print("\nDELETING STUDENT 4...")
    deleteStudent(4)

    print("\nUPDATED ALL STUDENTS:")
    getAllStudents()
