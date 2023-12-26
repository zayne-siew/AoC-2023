# with open('d2p1.txt') as f: print(sum(i+1 for i,k in enumerate([l.split(' ') for l in f.readlines()]) if all(int(k[j])<=12+('r','g','b').index(k[j+1][0]) for j in range(2,len(k),2))))

colours = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('d2p1.txt') as f:
    res = 0

    for i, line in enumerate(f.read().split('\n')):
        line = line[line.index(':') + 2:]
        for seq in line.split('; '):
            flag = False
            for s in seq.split(', '):
                n, colour = s.split(' ')
                if int(n) > colours[colour]:
                    flag = True
                    break
            if flag:
                break
        else:
            res += i + 1

    print(res)