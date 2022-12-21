a = 9
def func():
    global a
    a = 8
    print(a) 
    a = 900
    print(a)

print(a)
func()
print(a)