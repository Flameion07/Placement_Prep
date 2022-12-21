with open('file.txt', 'r') as f:
    text = f.read()

text = text.replace('donkey', "######")

with open('file.txt', 'w') as f:
    f.write(text)