from itertools import product

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
    grid = [list(f.readline().strip()) for _ in range(m)]
    start = None
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == 'S':
                start = (i, j)
                break
        if start is not None:
            break

    curr = [(start, (0, 0))]
    seen = set()
    while curr:
        new_curr = []
        for _ in range(len(curr)):
            (i, j), (di, dj) = curr.pop()
            if (i, j) == start and (di or dj):
                new_curr = []
                break
            new_curr.extend(((i + ni, j + nj), (-ni, -nj)) for ni, nj in d[grid[i][j]] - {(di, dj)} if 0 <= i + ni < m and 0 <= j + nj < n)
            seen.add((i, j))
        curr = new_curr

    new_grid = [['.' for _ in range(3 * n)] for _ in range(3 * m)]
    for i in range(m):
        for j in range(n):
            if (i, j) in seen:
                print(i, j, grid[i][j])
                if grid[i][j] == '-':
                    new_grid[3 * i][3 * j:3 * j + 3] = '...'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = 'XXX'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '...'
                elif grid[i][j] == '|':
                    new_grid[3 * i][3 * j:3 * j + 3] = '.X.'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = '.X.'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '.X.'
                elif grid[i][j] == 'F':
                    new_grid[3 * i][3 * j:3 * j + 3] = '...'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = '.XX'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '.X.'
                elif grid[i][j] == 'L':
                    new_grid[3 * i][3 * j:3 * j + 3] = '.X.'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = '.XX'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '...'
                elif grid[i][j] == '7':
                    new_grid[3 * i][3 * j:3 * j + 3] = '...'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = 'XX.'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '.X.'
                elif grid[i][j] == 'J':
                    new_grid[3 * i][3 * j:3 * j + 3] = '.X.'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = 'XX.'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '...'
                elif grid[i][j] == 'S':
                    new_grid[3 * i][3 * j:3 * j + 3] = '...'
                    new_grid[3 * i + 1][3 * j:3 * j + 3] = 'XXX'
                    new_grid[3 * i + 2][3 * j:3 * j + 3] = '...'

    print('\n'.join(''.join(row) for row in new_grid), end='\n\n')
    dfs = [(0, 0)]
    while dfs:
        i, j = dfs.pop()
        new_grid[i][j] = 'O'
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= i + di < 3 * m and 0 <= j + dj < 3 * n and new_grid[i + di][j + dj] == '.':
                dfs.append((i + di, j + dj))

    print('\n'.join(''.join(row) for row in new_grid))
    print(sum(all(new_grid[3 * i + di][3 * j + dj] == '.' for di, dj in product(range(3), repeat=2)) for i, j in product(range(m), range(n))))