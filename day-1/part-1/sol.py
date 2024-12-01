l, r = [], []
ans = 0

with open("../input.txt", "r") as file:
    lines = file.readlines()
    

for line in lines:
    inputs = line.split("  ")
    l.append(int(inputs[0]))
    r.append(int(inputs[1]))
    
l.sort()
r.sort()

for i in range(len(r)):
    ans += abs(l[i] - r[i])
    
print(ans)