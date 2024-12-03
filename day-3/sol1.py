import re

def solve_corrupted_memory(input_text):
    # Regular expression to match valid mul(X,Y) instructions
    # - Must start with exactly 'mul('
    # - Followed by 1-3 digits
    # - Then a comma
    # - Then 1-3 digits
    # - Then closing parenthesis
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches in the input text
    matches = re.finditer(pattern, input_text)
    
    total = 0
    # Process each valid multiplication instruction
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        result = x * y
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