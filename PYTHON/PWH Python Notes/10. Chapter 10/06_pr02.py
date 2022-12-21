
import math
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number

    def squareRoot(self):
        return math.sqrt(self.number)

    def cube(self):
        return self.number * self.number * self.number

two = Calculator(2)
print(two.number)
print(two.square())
print(two.cube())
print(two.squareRoot())