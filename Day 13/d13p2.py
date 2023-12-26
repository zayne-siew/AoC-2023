from itertools import product

with open('d13p1.txt') as f:
    lines = [grid.split() for grid in f.read().split('\n\n')]
    total = 0
    for grid in lines:
        m, n = len(grid), len(grid[0])
        grid = [list(line) for line in grid]
        prev = 0
        for i in range(1, m):
            if all(grid[i+k] == grid[i-1-k] for k in range(min(i, m-i))):
                print('row', i)
                prev = 100 * i
                break
        else:
            for i in range(1, n):
                if all(grid[j][i+k] == grid[j][i-1-k] for j in range(m) for k in range(min(i, n-i))):
                    print('col', i)
                    prev = i
                    break
        for a, b in product(range(m), range(n)):
            grid[a][b] = '#' if grid[a][b] == '.' else '.'
            res = 0
            for i in range(1, m):
                if i * 100 != prev and all(grid[i+k] == grid[i-1-k] for k in range(min(i, m-i))):
                    print('row', i)
                    res = 100 * i
                    break
            else:
                for i in range(1, n):
                    if i != prev and all(grid[j][i+k] == grid[j][i-1-k] for j in range(m) for k in range(min(i, n-i))):
                        print('col', i)
                        res = i
                        break
            if res:
                total += res
                break
            grid[a][b] = '#' if grid[a][b] == '.' else '.'
    print(total)