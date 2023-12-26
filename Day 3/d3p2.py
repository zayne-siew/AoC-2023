import re

with open('d3p1.txt') as f:
    grid = [line.strip() for line in f.readlines()]
    m, n = len(grid), len(grid[0])
    d = {(r, c): [] for r in range(m) for c in range(n) if grid[r][c] == '*'}
    for i, row in enumerate(grid):
        for num in re.finditer(r'\d+', row):
            j, k = num.span()
            for r, c in d:
                if abs(r - i) <= 1 and j - 1 <= c <= k:
                    d[(r, c)].append(int(num[0]))
    print(sum(v[0] * v[1] for v in d.values() if len(v) == 2))