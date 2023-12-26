data = [list(line.strip()) for line in open('d23p1.txt').readlines()]
edges = {}  # (r, c) -> (ar, ac, length)
for r, row in enumerate(data):
    for c, v in enumerate(row):
        if v in ".>v":
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ar, ac = r + dr, c + dc
                if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                    continue
                if data[ar][ac] in ".>v":
                    edges.setdefault((r, c), set()).add((ar, ac, 1))
                    edges.setdefault((ar, ac), set()).add((r, c, 1))

# Remove nodes with degree 2 by merging the edges
while True:
    for n, e in edges.items():
        if len(e) == 2:
            a, b = e
            edges[a[:2]].remove(n + (a[2],))
            edges[b[:2]].remove(n + (b[2],))
            edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
            edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
            del edges[n]
            break
    else:
        break

n, m = len(data), len(data[0])

q = [(0, 1, 0)]
visited = set()
best = 0
while q:
    r, c, d = q.pop()
    if d == -1:
        visited.remove((r, c))
        continue
    if (r, c) == (n - 1, m - 2):
        best = max(best, d)
        continue
    if (r, c) in visited:
        continue
    visited.add((r, c))
    q.append((r, c, -1))
    for ar, ac, l in edges[(r, c)]:
        q.append((ar, ac, d + l))
print(best)