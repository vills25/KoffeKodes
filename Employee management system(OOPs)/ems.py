import os

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.__salary = salary  # Encapsulation
    
    # Getter for salary
    def get_salary(self):
        return self.__salary
    
    # Setter for salary with exception handling
    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative!")
        self.__salary = new_salary

    # Display details method
    def display_details(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Dept: {self.department}, Salary: {self.__salary}"

# Derived class: Manager

class Manager(Employee):
    def __init__(self, name, emp_id, department, salary, team_size, project):
        super().__init__(name, emp_id, department, salary)
        self.team_size = team_size
        self.project = project

    # Overriding display details method # Recursion
    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Team Size: {self.team_size}, Project: {self.project}"

# Polymorphic Function

def show_details(employee):
    print(employee.display_details())

# File handling

def save_to_file(employee, filename="employee_data.txt"):
    with open(filename, "a") as file:
        file.write(employee.display_details() + "\n")
    print("\n Employee details saved!")


def load_from_file(filename="employee_data.txt"):
    if not os.path.exists(filename):
        print("\n No data found.")
        return
    print("\n Loaded Data from File:")
    with open(filename, "r") as file:
        for line in file:                 
            print(line.strip())

# Main Execution

def main():
    print("\n= Employee Management System =")
    while True:
        print("\n1. Add Employee")
        print("2. Add Manager")
        print("3. Display All Records from File")
        print("4. Exit")

        choice = input("\nChoose an option (1/2/3/4): ")
        
        if choice == '1':
            # Employee
            name = input("Enter Employee Name: ")
            emp_id = input("Enter Employee ID: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            
            emp = Employee(name, emp_id, department, salary)
            show_details(emp)
            save_to_file(emp)
        
        elif choice == '2':
            # Manager
            name = input("Enter Manager Name: ")
            emp_id = input("Enter Manager ID: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            team_size = int(input("Enter Team Size: "))
            project = input("Enter Project Name: ")
            
            mgr = Manager(name, emp_id, department, salary, team_size, project)
            show_details(mgr)
            save_to_file(mgr)
        
        elif choice == '3':
           
            load_from_file()
        
        elif choice == '4':
            print("\n Exiting...!")
            break
        
        else:
            print("\n Invalid Choice! Please try again.")

main()
