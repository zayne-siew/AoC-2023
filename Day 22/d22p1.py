from collections import defaultdict
from itertools import product

bricks = [tuple(tuple(map(int, corner.split(','))) for corner in line.strip().split('~')) for line in open('d22p1.txt').readlines()]
bricks.sort(key=lambda brick: min(brick[0][2], brick[1][2]))

grid = {}
final = []
down, up = defaultdict(set), defaultdict(set)
for start, end in bricks:
    x, y, z = map(lambda c: list(range(min(c), max(c) + 1)), zip(start, end))
    while z[0] > 1 and not any((a, b, c - 1) in grid for a, b, c in product(x, y, z)):
        z = [z[0] - 1] + z[:-1]

    brick = tuple(sorted({(a, b, c) for a, b, c in product(x, y, z)}))
    final.append(brick)
    z_min = min(z for _, _, z in brick)

    for x, y, z in brick:
        grid[x, y, z] = brick
        if z == z_min and (x, y, z - 1) in grid:
            down_brick = grid[x, y, z - 1]
            down[brick].add(down_brick)
            up[down_brick].add(brick)

print(sum(all(len(down[x]) > 1 for x in up[brick]) for brick in final))