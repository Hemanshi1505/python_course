# Final Project = Employee data

import json

employees = []


def add_employee():
    employee_id = input("Enter Employee ID: ")

    for employee in employees:
        if employee["EmployeeID"] == employee_id:
            print("Employee ID already exists!")
            return

    employee_name = input("Enter Employee Name: ")

    try:
        age = int(input("Enter Age: "))
        salary = float(input("Enter Basic Salary: "))

        if age <= 0 or salary < 0:
            print("Age and salary must be valid.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    department = input("Enter Department: ")
    position = input("Enter Position: ")

    employee = {
        "EmployeeID": employee_id,
        "EmployeeName": employee_name,
        "Age": age,
        "Department": department,
        "Position": position,
        "BasicSalary": salary,
    }

    employees.append(employee)

    print("Employee added successfully!")


def view_employees():
    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print("\n-----------------------------")
        print("Employee ID :", employee["EmployeeID"])
        print("Name        :", employee["EmployeeName"])
        print("Age         :", employee["Age"])
        print("Department  :", employee["Department"])
        print("Position    :", employee["Position"])
        print("Salary      :", employee["BasicSalary"])
        print("-----------------------------")


def search_employee():
    if not employees:
        print("No employees found.")
        return

    print("\n1. Search by Employee ID")
    print("2. Search by Name")
    print("3. Search by Department")

    choice = input("Enter choice: ")

    search_value = input("Enter search value: ").lower()

    found = False

    for employee in employees:

        if choice == "1":
            if employee["EmployeeID"].lower() == search_value:
                print_employee(employee)
                found = True

        elif choice == "2":
            if employee["EmployeeName"].lower() == search_value:
                print_employee(employee)
                found = True

        elif choice == "3":
            if employee["Department"].lower() == search_value:
                print_employee(employee)
                found = True

        else:
            print("Invalid choice.")
            return

    if not found:
        print("Employee not found.")


def print_employee(employee):
    print("\n-----------------------------")
    print("Employee ID :", employee["EmployeeID"])
    print("Name        :", employee["EmployeeName"])
    print("Age         :", employee["Age"])
    print("Department  :", employee["Department"])
    print("Position    :", employee["Position"])
    print("Salary      :", employee["BasicSalary"])
    print("-----------------------------")


def update_employee():
    employee_id = input("Enter Employee ID to update: ")

    for employee in employees:

        if employee["EmployeeID"] == employee_id:

            print("\n1. Name")
            print("2. Age")
            print("3. Department")
            print("4. Position")
            print("5. Salary")
            print("6. Cancel")

            choice = input("Enter choice: ")

            if choice == "1":
                employee["EmployeeName"] = input("Enter new name: ")

            elif choice == "2":
                try:
                    employee["Age"] = int(input("Enter new age: "))
                except ValueError:
                    print("Invalid age.")
                    return

            elif choice == "3":
                employee["Department"] = input("Enter new department: ")

            elif choice == "4":
                employee["Position"] = input("Enter new position: ")

            elif choice == "5":
                try:
                    employee["BasicSalary"] = float(input("Enter new salary: "))
                except ValueError:
                    print("Invalid salary.")
                    return

            elif choice == "6":
                print("Update cancelled.")
                return

            else:
                print("Invalid choice.")
                return

            print("Employee updated successfully!")
            return

    print("Employee not found.")


def delete_employee():
    employee_id = input("Enter Employee ID to delete: ")

    for employee in employees:

        if employee["EmployeeID"] == employee_id:

            print_employee(employee)

            confirm = input("Are you sure? (yes/no): ").lower()

            if confirm == "yes":
                employees.remove(employee)
                print("Employee deleted successfully!")
            else:
                print("Delete cancelled.")

            return

    print("Employee not found.")


def salary_statistics():
    if not employees:
        print("No employees found.")
        return

    salaries = []

    for employee in employees:
        salaries.append(employee["BasicSalary"])

    total_salary = sum(salaries)
    average_salary = total_salary / len(employees)
    highest_salary = max(salaries)
    lowest_salary = min(salaries)

    print("\n========== SALARY STATISTICS ==========")
    print("Total Employees :", len(employees))
    print("Total Salary    :", total_salary)
    print("Average Salary  :", average_salary)
    print("Highest Salary  :", highest_salary)
    print("Lowest Salary   :", lowest_salary)

    for employee in employees:
        if employee["BasicSalary"] == highest_salary:
            print("\nHighest Paid Employee:")
            print("Name   :", employee["EmployeeName"])
            print("Salary :", employee["BasicSalary"])
            break


def save_employees():
    try:
        with open("employees.json", "w") as file:
            json.dump(employees, file, indent=4)

        print("Employee data saved successfully!")

    except Exception as e:
        print("Error while saving:", e)


def load_employees():
    global employees

    try:
        with open("employees.json", "r") as file:
            employees = json.load(file)

        print(len(employees), "employees loaded successfully!")

    except FileNotFoundError:
        print("No saved employee data found.")

    except json.JSONDecodeError:
        print("Employee file contains invalid data.")

    except Exception as e:
        print("Error while loading:", e)


def main():

    load_employees()

    while True:

        print("\n====================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Salary Statistics")
        print("7. Save Employees")
        print("8. Load Employees")
        print("9. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            salary_statistics()

        elif choice == "7":
            save_employees()

        elif choice == "8":
            load_employees()

        elif choice == "9":

            confirm = input("Are you sure you want to exit? (yes/no): ").lower()

            if confirm == "yes":
                print("Thank you for using Employee Management System!")
                break

        else:
            print("Invalid choice. Please try again.")


main()
