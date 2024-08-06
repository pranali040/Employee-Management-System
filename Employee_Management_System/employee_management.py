import mysql.connector
from tabulate import tabulate

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql",
    database="employee_management"
)
cursor = conn.cursor()

def create_employee(first_name, last_name, department, position, salary, hire_date):
    query = "INSERT INTO employees (first_name, last_name, department, position, salary, hire_date) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, department, position, salary, hire_date)
    cursor.execute(query, values)
    conn.commit()

def read_employees():
    query = "SELECT * FROM employees"
    cursor.execute(query)
    result = cursor.fetchall()
    print(tabulate(result, headers=["ID", "First Name", "Last Name", "Department", "Position", "Salary", "Hire Date"], tablefmt="psql"))

def update_employee(employee_id, first_name, last_name, department, position, salary, hire_date):
    query = "UPDATE employees SET first_name=%s, last_name=%s, department=%s, position=%s, salary=%s, hire_date=%s WHERE employee_id=%s"
    values = (first_name, last_name, department, position, salary, hire_date, employee_id)
    cursor.execute(query, values)
    conn.commit()

def delete_employee(employee_id):
    query = "DELETE FROM employees WHERE employee_id=%s"
    cursor.execute(query, (employee_id,))
    conn.commit()

def main():
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("How many employees you want to add:-"))
            for i in range(n):
                print(f"{i+1} Employee Details:-")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                department = input("Enter department: ")
                position = input("Enter position: ")
                salary = input("Enter salary: ")
                hire_date = input("Enter hire date (YYYY-MM-DD): ")
                create_employee(first_name, last_name, department, position, salary, hire_date)

        elif choice == '2':
            read_employees()

        elif choice == '3':
            employee_id = input("Enter employee ID to update: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            department = input("Enter department: ")
            position = input("Enter position: ")
            salary = input("Enter salary: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            update_employee(employee_id, first_name, last_name, department, position, salary, hire_date)

        elif choice == '4':
            employee_id = input("Enter employee ID to delete: ")
            delete_employee(employee_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection
cursor.close()
conn.close()