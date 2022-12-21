# Sum(8) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
# Sum(n) = Sum(n-1) + n 
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n 

a = sum(5)
print(a)
