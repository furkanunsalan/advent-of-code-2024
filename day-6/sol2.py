from typing import List, Set, Tuple, Optional
from copy import deepcopy

def parse_map(input_map: str) -> Tuple[List[List[str]], Tuple[int, int], str]:
    grid = [list(line.strip()) for line in input_map.strip().splitlines()]
    direction = '^'
    guard_pos = None
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in '^v<>':
                guard_pos = (x, y)
                direction = grid[y][x]
                grid[y][x] = '.'  # Clear guard position in grid
                break
        if guard_pos:
            break
            
    if guard_pos is None:
        raise ValueError("No guard position (^v<>) found in the input map!")
            
    return grid, guard_pos, direction

def get_next_position(pos: Tuple[int, int], direction: str) -> Tuple[int, int]:
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
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]

def is_valid_position(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    x, y = pos
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False
    return True

def detect_loop(grid: List[List[str]], start_pos: Tuple[int, int], start_direction: str) -> bool:
    visited_states = set()  # Track (position, direction) states
    pos = start_pos
    direction = start_direction
    
    while True:
        # Create state tuple of current position and direction
        state = (pos, direction)
        
        # If we've seen this state before, we're in a loop
        if state in visited_states:
            return True
            
        visited_states.add(state)
        
        # Calculate next position
        next_pos = get_next_position(pos, direction)
        
        # Check if guard would move out of bounds
        if not is_valid_position(next_pos, grid):
            return False
            
        # Check if obstacle ahead
        x, y = next_pos
        if grid[y][x] == '#':
            # Turn right if obstacle
            direction = turn_right(direction)
        else:
            # Move forward if no obstacle
            pos = next_pos

def find_loop_positions(input_map: str) -> int:
    # Parse initial map
    grid, guard_pos, start_direction = parse_map(input_map)
    loop_positions = set()
    
    # Try placing an obstruction at each empty position
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # Skip if not empty space or guard starting position
            if grid[y][x] != '.' or (x, y) == guard_pos:
                continue
                
            # Create a copy of the grid with new obstruction
            test_grid = deepcopy(grid)
            test_grid[y][x] = '#'
            
            # Check if this creates a loop
            if detect_loop(test_grid, guard_pos, start_direction):
                loop_positions.add((x, y))
    
    return len(loop_positions)

def main():
    try:
        with open('input.txt', 'r') as file:
            puzzle_input = file.read()
        
        result = find_loop_positions(puzzle_input)
        print(f"Number of possible obstruction positions that create loops: {result}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check that the input file contains a valid map with a guard position (^v<>)")

if __name__ == "__main__":
    main()