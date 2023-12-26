with open('d4p1.txt') as f:
    total = 0
    for line in f.readlines():
        win, inp = map(lambda s: set(s.split()), line[line.index(':') + 2:].split(' | '))
        res = win & inp
        total += 2 ** (len(res) - 1) if res else 0
    print(total)