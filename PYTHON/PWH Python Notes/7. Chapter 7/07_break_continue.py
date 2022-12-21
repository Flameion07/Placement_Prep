a = [1,2,3,4,5]

for item in a:
    print(item)
    if(item == 3):
        continue
    print("done this iteration for ", item)    

print("We have finished this loop")