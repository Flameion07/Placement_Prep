oxford = {
    "gift": "Something willingly given to someone to appreciate",
    "this": "A keyword in c++",
    "Youtube": "A video sharing platform",
    "instagram": "a picture sharing platform",
    "mylist": [1, 3, 45]
}

oxford.update({"harry":"Good boy", "mylist": [56, 8]})
# print(oxford.items())
for a, b in oxford.items():
    print(a,":=", b)

# for key in oxford.keys():
#     print(key)