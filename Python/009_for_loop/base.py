x = int(input("enter your line length "))
y = input("do you want Vertical or Horizontal ")

if y == "Vertical":
    for z in range(0,x):
        print(z) 
elif y == "Horizontal":
    for z in range(0,x):
        print(z, end=",")
else:
    print("invalid input")