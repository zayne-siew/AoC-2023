import re

with open('d3p1.txt') as f:
    grid = [line.strip() for line in f.readlines()]
    m, n = len(grid), len(grid[0])
    total = 0
    for i, row in enumerate(grid):
        for num in re.finditer(r'\d+', row):
            j, k = num.span()
            if any(ch not in '0123456789.' for ch in ''.join(grid[r][max(j-1, 0):min(k+1, n)] for r in range(max(i-1, 0), min(i+2, m)))):
                total += int(num[0])
    print(total)