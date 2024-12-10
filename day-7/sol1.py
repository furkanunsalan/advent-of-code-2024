ans = 0

def checkOperations(target, values, nowValue, i):
    if (i >= len(values)):
        return target == nowValue
    return checkOperations(target, values, nowValue*values[i], i+1) or checkOperations(target, values, nowValue+values[i], i+1)

# Open the file, read lines and split every l,ne by ":"
with open("input.txt", "r") as file:
    lines = [line.strip().split(": ") for line in file.readlines()]

for line in lines:
    target = int(line[0])
    values = [int(m) for m in line[1].split(" ")]
    if checkOperations(target, values, 0, 0):
        ans += target


print(ans)