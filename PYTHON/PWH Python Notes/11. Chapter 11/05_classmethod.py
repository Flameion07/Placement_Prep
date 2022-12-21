class Employee:
    a = 10
    b = 4
    c = 6
    @classmethod
    def setAttrs(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c

emp = Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)
emp.setAttrs(1, 2, 3)
print(Employee.a)
print(Employee.b)
print(Employee.c)