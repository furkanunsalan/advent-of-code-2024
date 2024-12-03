import re

def solve_corrupted_memory(input_text):
    # Patterns for different instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    # Find all instructions with their positions
    instructions = []
    
    # Find multiplication instructions
    for match in re.finditer(mul_pattern, input_text):
        instructions.append({
            'type': 'mul',
            'pos': match.start(),
            'x': int(match.group(1)),
            'y': int(match.group(2))
        })
    
    # Find do() instructions
    for match in re.finditer(do_pattern, input_text):
        instructions.append({
            'type': 'do',
            'pos': match.start()
        })
    
    # Find don't() instructions
    for match in re.finditer(dont_pattern, input_text):
        instructions.append({
            'type': 'dont',
            'pos': match.start()
        })
    
    # Sort instructions by position to process them in order
    instructions.sort(key=lambda x: x['pos'])
    
    # Process instructions
    total = 0
    mul_enabled = True  # Multiplications are enabled at the start
    
    for instruction in instructions:
        if instruction['type'] == 'do':
            mul_enabled = True
        elif instruction['type'] == 'dont':
            mul_enabled = False
        elif instruction['type'] == 'mul' and mul_enabled:
            result = instruction['x'] * instruction['y']
            total += result
    
    return total

def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == "__main__":
    filename = "input.txt"
    puzzle_input = read_input_file(filename)
    if puzzle_input is not None:
        answer = solve_corrupted_memory(puzzle_input)
        print(answer)