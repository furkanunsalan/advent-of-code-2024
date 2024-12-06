from typing import List, Set, Tuple

def parse_map(input_map: str) -> Tuple[List[List[str]], Tuple[int, int], str]:
    # Convert input string to 2D grid and find guard position/direction
    grid = [list(line) for line in input_map.strip().splitlines()]
    direction = '^'
    guard_pos = None
    
    # Find guard's starting position
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in '^v<>':
                guard_pos = (x, y)
                direction = grid[y][x]
                grid[y][x] = '.'  # Clear guard position in grid
                break
        if guard_pos:
            break
            
    return grid, guard_pos, direction

def get_next_position(pos: Tuple[int, int], direction: str) -> Tuple[int, int]:
    # Calculate next position based on current direction
    x, y = pos
    if direction == '^':
        return (x, y - 1)
    elif direction == 'v':
        return (x, y + 1)
    elif direction == '>':
        return (x + 1, y)
    else:  # '<'
        return (x - 1, y)

def turn_right(direction: str) -> str:
    # Return new direction after turning right
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]

def is_valid_position(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    # Check if position is within grid bounds
    x, y = pos
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False
    return True

def simulate_guard_path(input_map: str) -> int:
    # Parse input map
    grid, guard_pos, direction = parse_map(input_map)
    visited = {guard_pos}  # Set to track visited positions
    
    while True:
        # Calculate next position
        next_pos = get_next_position(guard_pos, direction)
        
        # Check if guard would move out of bounds
        if not is_valid_position(next_pos, grid):
            break
            
        # Check if obstacle ahead
        x, y = next_pos
        if grid[y][x] == '#':
            # Turn right if obstacle
            direction = turn_right(direction)
        else:
            # Move forward if no obstacle
            guard_pos = next_pos
            visited.add(guard_pos)
            
    return len(visited)

# Read input from file
def main():
    with open('input.txt', 'r') as file:
        puzzle_input = file.read()
    
    result = simulate_guard_path(puzzle_input)
    print(f"Number of distinct positions visited: {result}")

if __name__ == "__main__":
    main()