# A very basic sample class
class Employee:
    name = "Harry"
    marks = 34
    center = "Delhi"

    def printObj(self):
        print(f"The name is {self.name}")



harry = Employee() # A basic object
shyam = Employee() # A basic object
print(harry.marks)
print(harry.center)
print(harry.name)
harry.printObj() # Employee.printObj(harry) 
# Employee.printObj(harry) 