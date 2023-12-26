from math import lcm
from functools import reduce
with open('d8p1.txt') as f:
    seq = f.readline().strip()
    n = len(seq)
    _ = f.readline()
    d = {}
    while (line := f.readline()):
        d[line[:3]] = (line[7:10], line[12:15])

    m = {}
    for c in d:
        if c[-1] != 'A':
            continue
        count = 0
        nxt = c
        while nxt[-1] != 'Z':
            nxt = d[nxt][seq[count % n] == 'R']
            count += 1
        m[c] = count
    print(m)
    print(lcm(*m.values()))