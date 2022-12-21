a = [1,2,3,4,5]

for item in a:
    print(item)
    if(item == 3):
        break
    print("done this iteration for ", item)    
else:
    print("We are inside else")
print("We have finished this loop")