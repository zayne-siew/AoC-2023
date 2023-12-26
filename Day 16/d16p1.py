from collections import deque, defaultdict

with open('d16p1.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
    m, n = len(grid), len(grid[0])
    q = deque([(0, -1, 0, 1)])
    seen = defaultdict(set)

    while q:
        i, j, di, dj = q.popleft()
        i += di
        j += dj
        if (di, dj) in seen[(i, j)]:
            continue
        seen[(i, j)].add((di, dj))
        if grid[i][j] == '\\':
            di, dj = dj, di
        elif grid[i][j] == '/':
            di, dj = -dj, -di
        elif (dj == 0 and grid[i][j] == '-') or (di == 0 and grid[i][j] == '|'):
            di, dj = dj, di
        if 0 <= i + di < m and 0 <= j + dj < n:
            q.append((i, j, di, dj))
        if (di == 0 and grid[i][j] == '-') or (dj == 0 and grid[i][j] == '|') and 0 <= i - di < m and 0 <= j - dj < n:
            q.append((i, j, -di, -dj))

    print(len(seen))