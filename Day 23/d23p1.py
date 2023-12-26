grid = [list(line.strip()) for line in open('d23p1.txt').readlines()]
m, n = len(grid), len(grid[0])
DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))

curr = [(0, 1, {(0, 1)})]
res = -1
while curr:
    nxt = []
    for i, j, seen in curr:
        if i == m - 1 and j == n - 2:
            continue
        for k, (di, dj) in enumerate(DIRS):
            if 0 <= i + di < m and 0 <= j + dj < n and (i + di, j + dj) not in seen and \
                    (grid[i + di][j + dj] == '.' or grid[i + di][j + dj] == '><v^'[k]):
                nxt.append((i + di, j + dj, seen | {(i, j)}))
    curr = nxt
    res += 1

print(res)