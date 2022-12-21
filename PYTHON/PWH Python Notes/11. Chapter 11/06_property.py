class Employee:
    a = 10
    b = 4
    c = 6
    @classmethod
    def setAttrs(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c

    @property
    def length(self):
        return self.a

    @length.setter 
    def length(self, value):
        self.a = value

emp = Employee() 
emp.setAttrs(1, 2, 3) 
print(emp.length)
emp.length = 78
print(emp.length)