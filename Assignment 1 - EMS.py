employee_storage = {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}

class EMS:
    def __init__(self,name="", age=0, department="", salary=0):
        self.name =name
        self.age =age
        self.department=department
        self.salary=salary
        
        
    def add_employee(self):
        while True:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employee_storage.keys():
                print(" ID already exists! Try again.\n")
            else:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                department = input("Enter Department: ")
                salary = int(input("Enter Salary: "))
                
                employee_storage[emp_id] = {
                    'name': name,
                    'age': age,
                    'department': department,
                    'salary': salary
                }
                print("\n Employee added successfully!\n")
                break
    def view_employees(self):
        if not employee_storage:
            print("\nNo employees found.\n")
        else:
            print("\n--- All Employees ---")
            for emp_id, details in employee_storage.items():
                print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, "
                      f"Department: {details['department']}, Salary: {details['salary']}")
            print()
    def search_employee(self):
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employee_storage:
            details = employee_storage[emp_id]
            print(f"\nID: {emp_id}, Name: {details['name']}, Age: {details['age']}, "
                  f"Department: {details['department']}, Salary: {details['salary']}\n")
        else:
            print("\n-- Employee not found! --\n")
        
    def menu(self):
        while True:
            print("""PRESS 1-Add Employee\nPRESS 2-View All Employees\nPRESS 3-Search for Employee\nPRESS 4-Exit\n""")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                self.add_employee()
            elif choice == 2:
                self.view_employees()
            elif choice == 3:
                self.search_employee()
            elif choice == 4:
                    print("Thank you for using the Employee Management System. Goodbye!")
                    break
            else:
                    print(" Invalid choice! Please try again.\n")

if __name__ == "__main__":
    EMS().menu()
