class MyClass:
    a = 9

obj = MyClass()
print(obj.a)
obj.a = 0 # I am setting an instance attribute by doing this!
print(obj.a)
print(MyClass.a)