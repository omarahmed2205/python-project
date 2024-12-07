import csv

class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary
        if email:
            self.email = email

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"

class EmployeeManager:
    def __init__(self, file_name="employees.csv"):
        self.file_name = file_name
        self.employees = []
        self.load_from_csv()

    def load_from_csv(self):
        try:
            with open(self.file_name, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp = Employee(row['ID'], row['Name'], row['Position'], row['Salary'], row['Email'])
                    self.employees.append(emp)
        except FileNotFoundError:
            with open(self.file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
                writer.writeheader()

    def save_to_csv(self):
        with open(self.file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
            writer.writeheader()
            for emp in self.employees:
                writer.writerow({
                    "ID": emp.emp_id,
                    "Name": emp.name,
                    "Position": emp.position,
                    "Salary": emp.salary,
                    "Email": emp.email
                })

    def add_employee(self, emp_id, name, position, salary, email):
        if any(emp.emp_id == emp_id for emp in self.employees):
            print("Employee ID already exists.")
            return
        emp = Employee(emp_id, name, position, salary, email)
        self.employees.append(emp)
        self.save_to_csv()
        print("Employee added successfully.")

    def update_employee(self, emp_id, name=None, position=None, salary=None, email=None):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.update_details(name, position, salary, email)
                self.save_to_csv()
                print("Employee updated successfully.")
                return
        print("Employee not found.")

    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                self.save_to_csv()
                print("Employee deleted successfully.")
                return
        print("Employee not found.")

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(emp.display())
                return
        print("Employee not found.")

    def list_all_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                print(emp.display())

def main():
    manager = EmployeeManager()
    while True:
        print("\nEmployee Data Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = input("Enter Employee Salary: ")
            email = input("Enter Employee Email: ")
            manager.add_employee(emp_id, name, position, salary, email)
        elif choice == "2":
            emp_id = input("Enter Employee ID to Update: ")
            print("Leave fields blank to keep current values.")
            name = input("Enter New Name: ")
            position = input("Enter New Position: ")
            salary = input("Enter New Salary: ")
            email = input("Enter New Email: ")
            manager.update_employee(emp_id, name or None, position or None, salary or None, email or None)
        elif choice == "3":
            emp_id = input("Enter Employee ID to Delete: ")
            manager.delete_employee(emp_id)
        elif choice == "4":
            emp_id = input("Enter Employee ID to Search: ")
            manager.search_employee(emp_id)
        elif choice == "5":
            manager.list_all_employees()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
