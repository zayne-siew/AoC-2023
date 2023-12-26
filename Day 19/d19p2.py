from math import prod

with open('d19p1.txt') as f:
    w = {}
    while (line := f.readline().strip()) != '':
        idx = line.index('{')
        name = line[:idx]
        instructions = [x.split(':') for x in line[idx + 1:-1].split(',')]
        for i, ((p, s, *c), nxt) in enumerate(instructions[:-1]):
            instructions[i] = (p, s == '>', int(''.join(c)), nxt)
        w[name] = instructions

    def dfs(curr, d):
        print(curr, d)
        if curr == 'R':
            return 0
        elif curr == 'A':
            return prod(_max - _min + 1 for _min, _max in d.values())

        res = 0
        for p, s, c, nxt in w[curr][:-1]:
            _min, _max = d[p]
            if s and _max > c:
                res += dfs(nxt, d | {p: (c + 1, _max)})
                _max = c
            elif not s and _min < c:
                res += dfs(nxt, d | {p: (_min, c - 1)})
                _min = c
            d[p] = (_min, _max)
        res += dfs(w[curr][-1][0], d)

        return res

    print(dfs('in', {p: (1, 4000) for p in 'xmas'}))