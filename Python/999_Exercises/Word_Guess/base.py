import random
list_words = []

with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)
        
awser = list_words[random.randrange(2315)]
a = 0
r = 6
for i in range(0,r):
    guess = input("guess a 5 letter word: ")
    if answer == guess:
        print("you won")
        break
    for j in range(2315):
        if(guess == list_words[j]) :
            a = a+1
    if(a>0):
        print("wrong answer")
    else:
        print("invalid word, guess again")
        r = r + 1
    a = 0
    print(answer)
    f.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        