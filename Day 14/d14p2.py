from itertools import product

def up(grid, m, n):
    new_grid = [['.' for _ in range(n)] for _ in range(m)]
    for j in range(n):
        curr = -1
        for i in range(m):
            if grid[i][j] == '#':
                curr = i
                new_grid[i][j] = '#'
            elif grid[i][j] == 'O':
                curr += 1
                new_grid[curr][j] = 'O'
    return new_grid

def down(grid, m, n):
    new_grid = [['.' for _ in range(n)] for _ in range(m)]
    for j in range(n):
        curr = m
        for i in range(m-1, -1, -1):
            if grid[i][j] == '#':
                curr = i
                new_grid[i][j] = '#'
            elif grid[i][j] == 'O':
                curr -= 1
                new_grid[curr][j] = 'O'
    return new_grid

def right(grid, m, n):
    new_grid = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        curr = n
        for j in range(n-1, -1, -1):
            if grid[i][j] == '#':
                curr = j
                new_grid[i][j] = '#'
            elif grid[i][j] == 'O':
                curr -= 1
                new_grid[i][curr] = 'O'
    return new_grid

def left(grid, m, n):
    new_grid = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        curr = -1
        for j in range(n):
            if grid[i][j] == '#':
                curr = j
                new_grid[i][j] = '#'
            elif grid[i][j] == 'O':
                curr += 1
                new_grid[i][curr] = 'O'
    return new_grid

def load(grid, m, n):
    total = 0
    for i, j in product(range(m), range(n)):
        if grid[i][j] == 'O':
            total += m - i
    return total

with open('d14p1.txt') as f:
    lines = [list(line) for line in f.read().split()]
    m, n = len(lines), len(lines[0])
    l = []
    c = 1000000000
    for i in range(c):
        grid = up(lines, m, n)
        #print('\n'.join(''.join(line) for line in grid), end='\n\n')
        grid = left(grid, m, n)
        #print('\n'.join(''.join(line) for line in grid), end='\n\n')
        grid = down(grid, m, n)
        #print('\n'.join(''.join(line) for line in grid), end='\n\n')
        grid = right(grid, m, n)
        #print('\n'.join(''.join(line) for line in grid))
        m1 = '\n'.join(''.join(line) for line in grid)
        if m1 in l:
            print(len(l))
            idx = l.index(m1)
            print(idx)
            mt = l[((c - idx - 1) % (len(l) - idx)) + idx]
            print(((c - idx - 1) % (len(l) - idx)) + idx)
            print(mt)
            print(load([list(line) for line in mt.split('\n')], m, n))
            break
        l.append(m1)
        lines = grid
    else:
        print(load(lines, m, n))