from math import prod

with open('d6p1.txt') as f:
    time = [int(x) for x in f.readline()[5:].strip().split()]
    dist = [int(x) for x in f.readline()[9:].strip().split()]
    res = [sum(x * (t-x) > d for x in range(1, t)) for t, d in zip(time, dist)]
    print(prod(res))