class Employee:
    def calculate_salary(self):
        print("Calculating salary...")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating manager's salary...")

# Demonstrate overridden behavior
employee = Employee()
manager = Manager()
employee.calculate_salary()
manager.calculate_salary()
