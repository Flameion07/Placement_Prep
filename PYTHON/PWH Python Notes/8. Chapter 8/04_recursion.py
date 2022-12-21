'''
factorial(n) = n * factorial(n-1)
factorial(0) = 1 (By definition)
factorial(4) = 4 X 3 X 2 X 1
factorial(3) = 3 X 2 X 1
factorial(13) = 13 X 12 X 11 X 10 X 9 X 8 X 7 X 6 X 5 X 4 X 3 X 2 X 1
'''

def factorial(n):
    # Base condition 
    if(n ==0 or n==1):
        return 1
    return n * factorial(n - 1) 

a = factorial(7)
print(a)