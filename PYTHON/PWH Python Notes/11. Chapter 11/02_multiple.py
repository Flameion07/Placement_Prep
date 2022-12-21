class Parent1:
    a = 4

class Parent2:
    b = 2

class Child(Parent1, Parent2):
    c = 9  

ch = Child()
print(ch.a)
print(ch.b)
print(ch.c)
