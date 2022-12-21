def process(l, word):
    word = word.strip()
    if word in l:
        l.remove(word) 
    return l1

l1 = ['harry', 'rohan', 'akash', 'shubham', 'lovish']
l1 = process(l1, '   rohan   ')
print(l1)