from collections import defaultdict

def hf(s):
    res = 0
    for ch in s:
        res = ((res + ord(ch)) * 17) % 256
    return res

with open('d15p1.txt') as f:
    lines = list(f.read().strip().split(','))
    d = defaultdict(list)
    for line in lines:
        if line[-1] == '-':
            line = line[:-1]
            h = hf(line)
            for i, (lbl, _) in enumerate(d[h]):
                if lbl == line:
                    d[h].pop(i)
                    break
        else:
            line, fl = line.split('=')
            h = hf(line)
            for i, (lbl, _) in enumerate(d[h]):
                if lbl == line:
                    d[h][i][1] = fl
                    break
            else:
                d[h].append([line, fl])
    print(d)
    total = 0
    for i, lst in d.items():
        for j, (_, fl) in enumerate(lst):
            total += (i + 1) * (j + 1) * int(fl)
    print(total)