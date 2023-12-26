def g(l):
    if all(x == 0 for x in l):
        return 0
    return l[0] - g([l[i+1] - l[i] for i in range(len(l)-1)])

with open('d9p1.txt') as f:
    lines = f.readlines()
    print(sum(g([int(x) for x in line.split()]) for line in lines))