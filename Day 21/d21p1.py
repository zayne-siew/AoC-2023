from itertools import product

grid = [list(line.strip()) for line in open('d21p1.txt').readlines()]
m, n = len(grid), len(grid[0])
start = None
for i, j in product(range(m), range(n)):
    if grid[i][j] == 'S':
        start = (i, j)
        break

curr = {start}
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(64):
    nxt = set()
    for (i, j), (di, dj) in product(curr, DIRS):
        if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] != '#':
            nxt.add((i + di, j + dj))
    curr = nxt

print(len(curr))