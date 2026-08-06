class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.emp_id == other.emp_id


emp1 = Employee(101, "Priyanka", 50000)
emp2 = Employee(101, "Mallika", 55000)
emp3 = Employee(102, "Manoj", 50000)

print(emp1 == emp2)  
print(emp1 == emp3)  