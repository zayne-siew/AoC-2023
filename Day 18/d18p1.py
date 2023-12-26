with open('d18p1.txt') as f:
    lines = [line.strip().split() for line in f.readlines()]
    i = j = steps = 0
    grid = [(i, j)]
    m = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for dr, ds, _ in lines:
        ds = int(ds)
        di, dj = m[dr]
        i += ds * di
        j += ds * dj
        grid.append((i, j))
        steps += ds

    inner = 0
    for i in range(len(grid) - 1):
        (a, b), (c, d) = grid[i:i + 2]
        inner += a * d - b * c  # shoelace algorithm

    print(abs(inner) // 2 + steps // 2 + 1)