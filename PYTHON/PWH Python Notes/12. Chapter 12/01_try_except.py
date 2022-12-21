try:
    print("Hello world")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
    if b>199:
        raise Exception("This number is too large")

except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("This is a zero division error")
except Exception as e:
    print(f"This problem occurred: {e}")
else:
    print("Try was successful")
    
print("There were no errors")