ans = 0

def concatenate(a, b):
    return int(f"{a}{b}")

def checkOperations(target, values, nowValue, i):
    
    if i >= len(values):
        return target == nowValue
    
    add_check = checkOperations(target, values, nowValue + values[i], i + 1)
    mult_check = checkOperations(target, values, nowValue * values[i], i + 1)
    concat_check = checkOperations(target, values, concatenate(nowValue, values[i]), i + 1) if nowValue != 0 else False
    
    return add_check or mult_check or concat_check

with open("input.txt", "r") as file:
    lines = [line.strip().split(": ") for line in file.readlines()]

for line in lines:
    target = int(line[0])
    values = [int(m) for m in line[1].split(" ")]
    # Check if the target can be achieved
    if checkOperations(target, values, 0, 0):
        ans += target

print(ans)
