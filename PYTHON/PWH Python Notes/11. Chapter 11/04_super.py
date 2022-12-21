class Parent:
    a = 4
    def __init__(self) -> None:
        print("Parent")

class Child1(Parent):
    b = 2
    def __init__(self) -> None:
        print("Child1")
        super().__init__()

class Child2(Child1):
    c = 9  
    def __init__(self) -> None:
        super().__init__()
        print("Child2")

ch = Child2()
print(ch.a)
print(ch.b)
print(ch.c)
