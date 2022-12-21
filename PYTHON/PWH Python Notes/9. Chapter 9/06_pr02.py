import random 

def game():
    score  =  random.randint(1, 100)
    print(f"The score is {score}")
    return score

score = game()
with open("hiscore.txt", "r") as f: 
    hiscore = int(f.read())

if hiscore<score:
    with open("hiscore.txt", "w") as f: 
        f.write(str(score))



