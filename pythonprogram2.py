class Employee:

    def __init__(self, emp_id, name, age, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.designation = designation
        self.salary = salary

    def display(self):
        print("\n----- Employee Details -----")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Department  :", self.department)
        print("Designation :", self.designation)
        print("Salary      :", self.salary)


# Creating employees

employee1 = Employee(
    "E101",
    "Rahul",
    25,
    "IT",
    "Software Developer",
    45000
)

employee2 = Employee(
    "E102",
    "Priya",
    28,
    "HR",
    "HR Manager",
    55000
)

employee3 = Employee(
    "E103",
    "Amit",
    30,
    "Finance",
    "Accountant",
    50000
)


# Display employees

employee1.display()
employee2.display()
employee3.display()