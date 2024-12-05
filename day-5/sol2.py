def parse_input(input_data):
    rules = []
    updates = []
    is_rules_section = True
    
    for line in input_data.strip().split('\n'):
        if not line:
            is_rules_section = False
            continue
        if is_rules_section:
            before, after = line.split('|')
            rules.append((int(before), int(after)))
        else:
            updates.append([int(x) for x in line.split(',')])
    
    return rules, updates

def build_graph(rules):
    # Build both forward and reverse adjacency lists
    graph = {}
    reverse_graph = {}
    
    # Initialize graphs with empty sets for all nodes
    all_nodes = set()
    for before, after in rules:
        all_nodes.add(before)
        all_nodes.add(after)
    
    for node in all_nodes:
        graph[node] = set()
        reverse_graph[node] = set()
    
    # Add edges to both graphs
    for before, after in rules:
        graph[before].add(after)
        reverse_graph[after].add(before)
    
    return graph, reverse_graph

def is_valid_order(update, graph):
    # Create position mapping
    positions = {num: i for i, num in enumerate(update)}
    
    # Check all dependencies
    for page in update:
        if page in graph:
            for must_come_after in graph[page]:
                if must_come_after in positions:
                    if positions[must_come_after] < positions[page]:
                        return False
    return True

def sort_update(update, graph, reverse_graph):
    # Create a subgraph containing only the pages in this update
    relevant_nodes = set(update)
    
    # Calculate initial in-degree for nodes in the update
    in_degree = {node: 0 for node in relevant_nodes}
    for node in relevant_nodes:
        for predecessor in reverse_graph[node]:
            if predecessor in relevant_nodes:
                in_degree[node] += 1
    
    # Initialize result and queue of nodes with no dependencies
    result = []
    queue = [node for node in relevant_nodes if in_degree[node] == 0]
    
    while queue:
        # Sort queue to ensure deterministic ordering when multiple nodes have no dependencies
        queue.sort(reverse=True)  # Higher numbers first if multiple options available
        node = queue.pop()
        result.append(node)
        
        # Update in-degrees
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in relevant_nodes:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
    
    return result

def find_middle_page(update):
    return update[len(update) // 2]

def solve_part2(input_data):
    rules, updates = parse_input(input_data)
    graph, reverse_graph = build_graph(rules)
    
    total = 0
    for update in updates:
        # Only process updates that are not already correctly ordered
        if not is_valid_order(update, graph):
            sorted_update = sort_update(update, graph, reverse_graph)
            middle = find_middle_page(sorted_update)
            total += middle
    
    return total

def main(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
    return solve_part2(input_data)

if __name__ == "__main__":
    file_path = 'input.txt'
    result = main(file_path)
    print(f"The sum of middle pages in corrected updates is: {result}")