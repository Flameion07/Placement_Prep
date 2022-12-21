oxford = {
    "lakdi": "wood",
    "kursi": "chair",
    "chaku": "knife"
}
key = input("Enter the key\n")
if(oxford.get(key)== None):
    print("Value not found")
else:
    print("The value corresponding to your key is:", oxford.get(key))