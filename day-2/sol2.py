def is_safe_report(report):
    levels = list(map(int, report.split())) # split the lines
    
    if len(levels) < 2:
        return False  # A report with less than 2 levels can't be safe
    
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    if not (increasing or decreasing):
        return False  # Not all increasing or all decreasing
    
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False  # Difference is out of bounds
    
    return True

def can_be_safe_by_removing_one(report):
    levels = list(map(int, report.split()))
    
    for i in range(len(levels)):
        # Create a new list without the i-th level
        modified_levels = levels[:i] + levels[i+1:]
        
        # Check if the modified report is safe
        if is_safe_report(' '.join(map(str, modified_levels))):
            return True  # It can be made safe by removing this level
    
    return False  # No single removal can make it safe

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report) or can_be_safe_by_removing_one(report):
            safe_count += 1
    return safe_count

with open('input.txt', 'r') as file:
    reports = file.readlines()

reports = [report.strip() for report in reports if report.strip()]  # Remove empty lines
safe_reports_count = count_safe_reports(reports)

print(safe_reports_count)