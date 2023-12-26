with open('d19p1.txt') as f:
    w = {}
    while (line := f.readline().strip()) != '':
        idx = line.index('{')
        name = line[:idx]
        instructions = [x.split(':') for x in line[idx + 1:-1].split(',')]
        for i, ((p, s, *c), nxt) in enumerate(instructions[:-1]):
            instructions[i] = (p, s == '>', int(''.join(c)), nxt)
        w[name] = instructions

    total = 0
    while (line := f.readline().strip()) != '':
        obj = {p: int(''.join(c)) for p, _, *c in line[1:-1].split(',')}
        curr = 'in'
        while curr != 'R' and curr != 'A':
            for p, s, c, nxt in w[curr][:-1]:
                if (s and obj[p] > c) or (not s and obj[p] < c):
                    curr = nxt
                    break
            else:
                curr = w[curr][-1][0]

        if curr == 'A':
            total += sum(obj.values())

    print(total)