class Complex:
    def __init__(self,a, b) -> None:
        self.a = a
        self.b = b

    def __add__(self, obj):
        return Complex(self.a + obj.a, self.b + obj.b)


c1 = Complex(1, 4)
c2 = Complex(11, 3)
c3 = c1+c2
print(c3.a, c3.b)