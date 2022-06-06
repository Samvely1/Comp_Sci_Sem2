x = input("what is your first and last name? ")
y = len(x)
v = 0
for z in range(0,y):
    c = x[v:v+1]
    v = v + 1
    print(c)