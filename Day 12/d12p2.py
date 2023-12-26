from functools import cache

@cache
def dfs(s, l, b):
    if not l:
        return int(s.find('#') == -1)
    elif not s:
        return int(len(l) == 0)
    res = 0
    if s[0] != '.':
        if l[0] == 1 and len(s) > 1 and s[1] == '#':
            if b:
                return 0
        else:
            res += dfs(s[1 + (l[0] == 1):], ((l[0] - 1,) if l[0] > 1 else tuple([])) + l[1:], l[0] > 1)
    if s[0] != '#':
        if b:
            if s[0] == '.':
                return 0
        else:
            res += dfs(s[1:], l, b)
    return res

with open('d12p1.txt') as f:
    lines = [line.strip().split() for line in f.readlines()]
    print(sum(dfs(s + '?' + s + '?' + s + '?' + s + '?' + s, tuple(int(x) for x in l.split(',')) * 5, False) for s, l in lines))