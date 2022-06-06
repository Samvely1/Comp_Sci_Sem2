x = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
count = 0

for i in range(len(x)):
    if x[i:i+5] == 'whale':
        count = count + 1
print(count) 
    


with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for i in range(len(x)):
            if x[i:i+5] == 'whale':
                count = count + 1
print(count)

f.close()
