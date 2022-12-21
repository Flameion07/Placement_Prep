class Employee:
    a = 34


class Programmer(Employee):
    b = 32

pr = Programmer()
print(pr.a)
print(pr.b)

em = Employee()
print(em.a)
# print(em.b) # This line throws an error