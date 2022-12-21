def is_divisible(n):
    if n%5 ==0:
        return True 
    return False

a = [1,2,3,4,5,60,7,8,9,10]
print(list(filter(is_divisible, a)))
