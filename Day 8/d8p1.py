with open('d8p1.txt') as f:
    seq = f.readline().strip()
    n = len(seq)
    _ = f.readline()
    d = {}
    while (line := f.readline()):
        d[line[:3]] = (line[7:10], line[12:15])
    count = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        curr = d[curr][seq[count % n] == 'R']
        count += 1
    print(count)