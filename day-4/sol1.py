def count_xmas_occurrences(grid):
    word = "XMAS"
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Directions: (dy, dx)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    for y in range(rows):
        for x in range(cols):
            for dy, dx in directions:
                # Check if we can find the word in this direction
                found = True
                for i in range(word_length):
                    ny = y + dy * i
                    nx = x + dx * i
                    if ny < 0 or ny >= rows or nx < 0 or nx >= cols or grid[ny][nx] != word[i]:
                        found = False
                        break
                if found:
                    count += 1

    return count

# Read the input from input.txt
with open('input.txt', 'r') as file:
    word_search = [line.strip() for line in file.readlines()]

# Count occurrences of "XMAS"
result = count_xmas_occurrences(word_search)
print(result)
