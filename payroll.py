# Employee payroll system

# List to hold employee data
employees = []

# Function to add an employee
def add_employee(employees, name, salary):
    return employees + [{"name": name, "salary": salary}]

# Function to calculate total payroll
def calculate_total_payroll(employees):
    return sum(employee["salary"] for employee in employees if employee["salary"] > 0)

# Usage example
employees = add_employee(employees, "Joseph", 1000)
employees = add_employee(employees, "Habiba", 2000)
total_payroll = calculate_total_payroll(employees)

print("Total Payroll:", total_payroll)
print("Employees:", employees)

# Employee class definition
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Creating an Employee instance
emp1 = Employee("Bob", 40000)  # Salary should be an integer
print(f"{emp1.name}: {emp1.salary}")

# Payroll class definition
class Payroll:
    def __init__(self, employees):
        self.employees = employees

    def total_payroll(self):
        return sum(employee["salary"] for employee in self.employees)

# Example of using the Payroll class
payroll = Payroll(employees)
print("Total Payroll from Payroll Class:", payroll.total_payroll())
