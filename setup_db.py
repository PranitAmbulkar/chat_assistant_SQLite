import sqlite3


def create_database():
    connection = sqlite3.connect("chat_assistant.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary INTEGER NOT NULL,
            Hire_Date TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Manager TEXT NOT NULL
        )
    ''')

    cursor.executemany(
        """
    INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)
""", [('Alice', 'Sales', 50000, '2021-01-15'),
      ('Bob', 'Engineering', 70000, '2020-06-10'),
      ('Charlie', 'Marketing', 60000, '2022-03-20'),
      ('Diana', 'HR', 80000, '2019-08-12'),
      ('Eve', 'Finance', 55000, '2021-07-01'),
      ('Frank', 'Operations', 65000, '2023-01-05'),
      ('Grace', 'Engineering', 75000, '2020-03-15'),
      ('Hank', 'Sales', 52000, '2022-11-10'),
      ('Ivy', 'Marketing', 61000, '2021-09-25'),
      ('Jack', 'Sales', 57000, '2023-05-18')])

    # Insert sample data into Departments table
    cursor.executemany(
        """
INSERT INTO Departments (Name, Manager) VALUES (?, ?)
""", [('Sales', 'Alice'), ('Engineering', 'Bob'), ('Marketing', 'Charlie'),
      ('HR', 'Diana'), ('Finance', 'Eve'), ('Operations', 'Frank')])

    # Commit changes and close the connection
    connection.commit()
    connection.close()


print("Database setup completed successfully!")
