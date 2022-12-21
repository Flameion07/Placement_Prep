class Parent:
    a = 4

class Child1(Parent):
    b = 2

class Child2(Child1):
    c = 9  

ch = Child2()
print(ch.a)
print(ch.b)
print(ch.c)
