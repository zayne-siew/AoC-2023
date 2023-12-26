with open('d14p1.txt') as f:
    lines = [list(line) for line in f.read().split()]
    m, n = len(lines), len(lines[0])
    total = 0
    for j in range(n):
        curr = -1
        for i in range(m):
            if lines[i][j] == '#':
                curr = i
            elif lines[i][j] == 'O':
                curr += 1
                total += m - curr
    print(total)