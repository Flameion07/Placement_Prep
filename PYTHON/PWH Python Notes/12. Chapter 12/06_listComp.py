l1 = [1, 2, 3, 4, 5, 6]

# l2 =[]
# for item in l1:
#     l2.append(item*item)

l2 = [i*i for i in l1 if i>2]
print(l2)