class Programmer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

harry = Programmer("Harry", "Python")
rohan = Programmer("Rohan", "Java")

print(rohan.name)
print(harry.name)