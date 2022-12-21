class Employee:
    def __init__(self, a, name) -> None:
        self.a = a
        self.name = name

    def __add__(self, obj):
         return self.a + obj.a

    def __str__(self) -> str:
        return self.name

    def __len__(self):
        return self.a

a = Employee(45, "Harry")
b = Employee(40, "Rohan")

print(a, b)
print(len(a))
print(len(b))