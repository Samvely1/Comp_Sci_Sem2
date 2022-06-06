mynumbers = [6,9,32,28,15,22,3,18]
high = 0
for i in mynumbers:
    if i > high:
        high = i
print(high)

mynumbers = [6,9,32,28,15,22,3,18]
low = 100
for i in mynumbers:
    if i <low:
        low = i
print(low)

mynumbers = [6,9,32,28,15,22,3,18]
a = 0

for i in mynumbers:
    a+=i
average = a / float(len(mynumbers))
print(average)