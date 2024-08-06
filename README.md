# Employee-Management-System

This project is a simple Employee Management System built using Python and MySQL, with the `tabulate` library for displaying data in a tabular format. 

It provides functionality to create, read, update, and delete employee records.

## Features

- **Add Employee**: Add new employee records with details such as first name, last name, department, position, salary, and hire date.
- **View Employees**: Display all employee records in a tabular format.
- **Update Employee**: Update the details of an existing employee.
- **Delete Employee**: Delete a specific employee record.

## Requirements

- Python 3.x
- MySQL
- MySQL Connector for Python
- Tabulate library for Python

## Install the required Python packages:

    pip install mysql-connector-python tabulate

## Set up the MySQL database:
1. Create a new database called employee_management:
    ```sql
   CREATE DATABASE employee_management;
     ```
    
2. Create a table called `employees` :
    ```sql
    USE employee_management;
    CREATE TABLE employees (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        department VARCHAR(255),
        position VARCHAR(255),
        salary DECIMAL(10, 2),
        hire_date DATE
    );
    ```

3. Update the connection settings in the Python script with your MySQL credentials:
    ```python
    conn = mysql.connector.connect(
        host="localhost",  # change to your host
        user="root",       # change to your user
        password="password",  # change to your password
        database="employee_management"  # change to your database
    )
    ```

## Screenshot

1) Details of all employees 
![option1](https://github.com/user-attachments/assets/84f2d20c-e9e8-423f-9319-0a55016aaa7d)

2) Adding details of new employee 
![option2](https://github.com/user-attachments/assets/21491104-1147-4290-857f-5879bfa7a635)

3) Updating details of an employee 
![option3](https://github.com/user-attachments/assets/38011159-3576-45f7-bba1-5c6070db304b)

4) Store data in Mysql
![option4](https://github.com/user-attachments/assets/8ae0b30a-9002-45f8-89e0-f71e8ee89aa7)
