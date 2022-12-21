# A very basic sample class
class Employee:
    name = "Harry" # A class attribute
    marks = 34
    center = "Delhi"

    def printObj(self):
        print(f"The name is {self.name}")
    
    @staticmethod
    def greet():
        print("good day")


Employee.name = "HarryNew" # Setting a class attribute for Employee
harry = Employee() # A basic object
shyam = Employee() # A basic object
print(harry.name) 
print(shyam.name)
shyam.name = "Shyam" # Setting an instance attribute to shyam
print(shyam.name)
print(harry.name)
harry.greet()
Employee.greet()