class Vector2d:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def printVector(self):
        print(f"{self.i}i + {self.j}j")

class Vector3d(Vector2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 
 

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"

 
v3 = Vector3d(11, 5, 9) 
print(v3)