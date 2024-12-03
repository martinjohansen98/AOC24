def main():
    with open("input.txt") as f:
        lines = f.readlines()

    total_safe = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if check_safety(levels):
            total_safe += 1
    print(total_safe)
    return total_safe

def is_valid_sequence(lst):
    increasing = all(0 < lst[i+1] - lst[i] <= 3 for i in range(len(lst) - 1))
    decreasing = all(0 < lst[i] - lst[i+1] <= 3 for i in range(len(lst) - 1))
    return increasing or decreasing

def check_safety(levels):
    if is_valid_sequence(levels):
        return True

    for i in range(len(levels)):
        modified = levels[:i] + levels[i+1:]
        if is_valid_sequence(modified):
            return True
        
    return False

main()
