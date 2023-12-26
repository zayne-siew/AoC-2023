with open('d5p1.txt') as f:
    seeds = [int(x) for x in f.readline().strip()[7:].split()]
    _ = f.readline()

    for _ in range(7):
        ns = [None for _ in range(len(seeds))]
        _ = f.readline()
        while (line := f.readline()) != '\n':
            a, b, c = map(int, line.strip().split())
            for i, x in enumerate(seeds):
                if b <= x < b + c:
                    ns[i] = (a - b) + x
            for i, xs in enumerate(ns):
                if xs is None:
                    ns[i] = seeds[i]
        seeds = ns

    print(min(seeds))