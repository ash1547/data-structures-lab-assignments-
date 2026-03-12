Lines changed: 34 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,34 @@
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary
    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        Employee.__init__(self, name, age, employee_id, salary)
        self.department = department
    def display_manager(self):
        print("Department:", self.department)
m1 = Manager("Divy",25, "E101",100000, "CSE")
print("Manager Details:")
m1.display_person()
m1.display_employee()
m1.display_manager()
