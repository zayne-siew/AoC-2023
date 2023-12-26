from heapq import heappop, heappush

grid = [[int(x) for x in line.strip()] for line in open('d17p1.txt').readlines()]
m, n = len(grid), len(grid[0])
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
seen = set()
costs = {}
q = [(0, 0, 0, -1)]

while q:
	cost, i, j, dd = heappop(q)
	if i == m - 1 and j == n - 1:
		print(cost)
		break
	elif (i, j, dd) in seen:
		continue
	seen.add((i, j, dd))
	for dr in range(4):
		cost_inc = 0
		if dr == dd or (dr + 2) % 4 == dd:
			continue
		for ds in range(1, 11):
			ni = i + DIRS[dr][0] * ds
			nj = j + DIRS[dr][1] * ds
			if not (0 <= ni < m and 0 <= nj < n):
				continue
			cost_inc += grid[ni][nj]
			if ds < 4 or costs.get((ni, nj, dr), float('inf')) <= cost + cost_inc:
				continue
			costs[(ni, nj, dr)] = cost + cost_inc
			heappush(q, (cost + cost_inc, ni, nj, dr))