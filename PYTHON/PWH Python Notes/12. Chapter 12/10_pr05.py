num = int(input("Enter a number: "))

multiplication = [i*num for i in range(1, 11)]
print(multiplication)

with open('mul.txt', 'w') as f:
    f.write(str(multiplication))