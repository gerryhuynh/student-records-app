# student-records-app

### Description

**Name (Student Number):** Gerry Huynh (100996769)

Created for COMP3005 Assignment 3 Question 1 - Winter 2024

This is a simple Python3 application that manages student records from a PostgreSQL database.

[Video Demo Link](https://youtu.be/jMeabRbVaAY)

### PostgreSQL Database setup

- Open pgAdmin 4
- Create a new database in pgAdmin 4
  - This can be called anything, such as `students`
- Using the query tool for the newly created database, open and run the included `students-setup.sql` file in pgAdmin 4
- This creates the `students` table and inserts the initial data

(optional) Run the following in the query tool to test that the query executed properly

```SQL
SELECT * FROM students;
```

- Should see all the expected columns and inserted data from `students-setup.sql`

### Install Python dependencies

Install [psycopg 3](https://pypi.org/project/psycopg/)

```bash
pip install --upgrade pip           # to upgrade pip
pip install "psycopg[binary,pool]"  # to install package and dependencies
```

### How to run

1. Update the connection setting variable values at the top of `manageStudentRecords.py` to match your PostgreSQL database connection information.

2. Run the following command in the terminal:

```bash
python3 ./manageStudentRecords.py
```
