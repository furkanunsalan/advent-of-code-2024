l, r = [], []
ans = 0

with open("../input.txt", "r") as file:
    lines = file.readlines()
    

for line in lines:
    inputs = line.split("  ")
    l.append(int(inputs[0]))
    r.append(int(inputs[1]))
    
dict = {}

for i in range(len(r)):
    dict[r[i]] = dict.get(r[i], 0) + 1
    
for i in l:
    ans += i * dict.get(i, 0)
    
print(ans)