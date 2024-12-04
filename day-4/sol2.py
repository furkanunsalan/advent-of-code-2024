with open("input.txt", "r") as file:
    content = [line.strip() for line in file.readlines()]

ans = 0

for j in range(len(content)):
    for i in range(len(content[0])):
        if i >= 1 and i < len(content[0])-1 and j >= 1 and j < len(content)-1:
            firstDiagonal = content[i+1][j+1]+content[i][j]+content[i-1][j-1]
            secondDiagonal = content[i-1][j+1]+content[i][j]+content[i+1][j-1]
            if (firstDiagonal == secondDiagonal or firstDiagonal == secondDiagonal[::-1]) and (firstDiagonal == "MAS" or firstDiagonal == "SAM"):
                ans += 1
print(ans)