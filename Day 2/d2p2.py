with open('d2p1.txt') as f:
    res = 0

    for i, line in enumerate(f.read().split('\n')):
        line = line[line.index(':') + 2:]
        r = g = b = 0
        for seq in line.split('; '):
            for s in seq.split(', '):
                n, colour = s.split(' ')
                if colour == 'red':
                    r = max(r, int(n))
                elif colour == 'blue':
                    b = max(b, int(n))
                else:
                    g = max(g, int(n))
        res += r * g * b

    print(res)