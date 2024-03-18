import psycopg

# PostgresSQL DB connection settings
### !!! Update these settings to match your local PostgresSQL settings !!! ###
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


# Displays main menu and gets user choice
# Returns the user's menu choice
def main_menu():
    print("\n1. Get all students")
    print("2. Add a new student")
    print("3. Update a student's email")
    print("4. Delete a student")
    print("0. Exit")
    choice = input("Enter your choice: ")
    print("\n")
    return choice


# Prompts the user for inputs and calls the appropriate function
# Returns nothing
def user_prompt():
    while True:
        choice = main_menu()

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            # get the student's information
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            enrollment_date = input(
                "Enter the student's enrollment date (YYYY-MM-DD): "
            )

            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            # get the student's id and new email
            student_id = input("Enter the student's id: ")
            new_email = input("Enter the student's new email: ")

            updateStudentEmail(student_id, new_email)
        elif choice == "4":
            # get the student's id
            student_id = input("Enter the student's id: ")

            deleteStudent(student_id)
        elif choice == "0" or choice.lower() == "exit":
            # exit the program
            break
        else:
            print("Invalid choice")


# Main function
# Calls the user_prompt function
if __name__ == "__main__":
    user_prompt()
