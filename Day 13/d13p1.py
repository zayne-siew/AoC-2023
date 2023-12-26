with open('d13p1.txt') as f:
    lines = [grid.split() for grid in f.read().split('\n\n')]
    total = 0
    for grid in lines:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            if all(grid[i+k] == grid[i-1-k] for k in range(min(i, m-i))):
                print('row', i)
                total += 100 * i
                break
        else:
            for i in range(1, n):
                if all(grid[j][i+k] == grid[j][i-1-k] for j in range(m) for k in range(min(i, n-i))):
                    print('col', i)
                    total += i
                    break
    print(total)