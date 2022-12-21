n = int (input("Enter a number"))
for i in range(1, n):
    # print(n-i, i)
    for j in range(n-i):
        print(" ", end="")

    for k in range(2*i-1):
        print("*", end="")

    for l in range(n-i):
        print(" ", end="")

    print("\n", end="")
