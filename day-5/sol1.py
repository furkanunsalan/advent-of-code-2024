def parse_input(input_data):
    rules = []
    updates = []
    is_rules_section = True
    
    for line in input_data.strip().split('\n'):
        if line == '':
            is_rules_section = False
            continue
        if is_rules_section:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def build_graph(rules):
    from collections import defaultdict
    
    graph = defaultdict(set)
    for x, y in rules:
        graph[x].add(y)
    
    return graph

def is_ordered(update, graph):
    index_map = {page: i for i, page in enumerate(update)}
    
    for x in graph:
        for y in graph[x]:
            if x in index_map and y in index_map:
                if index_map[x] > index_map[y]:  # x must come before y
                    return False
    return True

def find_middle_page(update):
    n = len(update)
    return update[n // 2]  # Middle page (lower middle if even)

def main(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
    
    rules, updates = parse_input(input_data)
    graph = build_graph(rules)
    
    total_middle_pages = 0
    
    for update in updates:
        if is_ordered(update, graph):
            middle_page = find_middle_page(update)
            total_middle_pages += middle_page
    
    return total_middle_pages

# Specify the path to your input file
file_path = 'input.txt'  # Change this to the path of your input file

# Run the solution
result = main(file_path)
print(result)  # Output will depend on the contents of the input file
