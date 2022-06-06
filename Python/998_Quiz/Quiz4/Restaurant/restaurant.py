import random

mylist = ["popeyes","mcdanalds","chipotle"]
cptlist = ["burrito","bowl", "chips"]

mclist = ["chicken nuggets","big mac","happy meal"]
poplist = ["chicken tenders","chicken sandwich", "mac and cheese" ]

x = random.choice(mylist)
print(x)
if x == "popeyes":
    y = random.choice(poplist)
    print(y)
elif x == "mcdanalds":
    z = random.choice(mclist)
    print(z)
elif x == "chipotle" :
    c = random.choice(cptlist)
    print(c)
    