import sys

m, n = 140, 141
d = {
    '|': {(-1, 0), (1, 0)},
    '-': {(0, -1), (0, 1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    '7': {(1, 0), (0, -1)},
    'F': {(1, 0), (0, 1)},
    'S': {(0, 1), (0, -1)},
    '.': set()
}

with open('d10p1.txt') as f:
    grid = [f.readline().strip() for _ in range(m)]
    start = None
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == 'S':
                start = (i, j)
                break
        if start is not None:
            break

    res = 0
    curr = [(start, (0, 0))]
    while curr:
        new_curr = []
        for _ in range(len(curr)):
            (i, j), (di, dj) = curr.pop()
            if (i, j) == start and res:
                print(res // 2)
                sys.exit(0)
            new_curr.extend(((i + ni, j + nj), (-ni, -nj)) for ni, nj in d[grid[i][j]] - {(di, dj)} if 0 <= i + ni < m and 0 <= j + nj < n)
        curr = new_curr
        res += 1