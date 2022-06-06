x = int(input("how many items are you buyings "))
a=0

for c in range(0,x):
    y = input("what item are you purchasing ")
    z = int(input("how much is the item "))
    print("thank you for purchasing " + y)
    a = a+z
    print("___________________________________________________")
print("Your total is :")
print(a)
