try:
    print("Hello world")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a/b
    

except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    c = "Infinite"
except Exception as e:
    print(f"This problem occurred: {e}") 
    
print(c)