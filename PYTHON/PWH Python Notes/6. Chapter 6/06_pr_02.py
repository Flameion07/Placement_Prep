m1 = int(input("Enter the marks for sub 1: "))
m2 = int(input("Enter the marks for sub 2: "))
m3 = int(input("Enter the marks for sub 3: "))

overAll = (m1+m2+m3)/3

if(overAll>=40):
    if(m1>=33 and m2>=33 and m3>=33):
        print("You have passed the exam")
    else:
        print("You have not passed the exam due to one of the subjects")
else:
    print("You have not passed the exam due to overall percentage")