from itertools import product, combinations

m = n = 140

with open('d11p1.txt') as f:
    lines = [f.readline().strip() for _ in range(m)]
    rows = {i for i in range(m) if lines[i] == '.' * n}
    cols = {i for i in range(n) if all(line[i] == '.' for line in lines)}
    galaxies = [(i, j) for i, j in product(range(m), range(n)) if lines[i][j] == '#']
    total = 0
    for (i1, j1), (i2, j2) in combinations(galaxies, 2):
        total += abs(i1 - i2) + abs(j1 - j2) + sum(min(i1, i2) < x < max(i1, i2) for x in rows) + sum(min(j1, j2) < x < max(j1, j2) for x in cols)
    print(total)