class Vector:
    def __init__(self, l1) -> None: 
        self.data = l1

    def __add__(self, obj):
        myList = []
        for i in range(len(obj.data)):
            myList.append(obj.data[i] + self.data[i])
        return Vector(myList)

    def __mul__(self, obj):
        dot = 0
        for i in range(len(obj.data)):
            dot += (obj.data[i] * self.data[i])
        return dot 
    def __len__(self):
        return len(self.data)

v1 = Vector([1, 2, 3])
v2 = Vector([11, 12, 13])
v3 = v1 + v2
v4 = v1*v2 # v4 is a scalar
print(v3.data)
print(v4)
print(len(v3))