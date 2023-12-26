from collections import defaultdict

with open('d4p1.txt') as f:
    res = defaultdict(int)
    lines = f.readlines()
    for i, line in enumerate(lines):
        res[i] += 1
        win, inp = map(lambda s: set(s.split()), line[line.index(':') + 2:].split(' | '))
        for nxt in range(1, len(win & inp) + 1):
            res[i + nxt] += res[i]
    print(sum(v for k, v in res.items() if k < len(lines)))