with open('d5p1.txt') as f:
    seeds = list(int(x) for x in f.readline().strip()[7:].split())
    seeds = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
    _ = f.readline()

    for _ in range(7):
        ns = [None for _ in range(len(seeds))]
        _ = f.readline()
        while (line := f.readline()) != '\n':
            a, b, c = map(int, line.strip().split())
            for i in range(len(seeds)):
                d, e = seeds[i]
                if d + e <= b or b + c <= d:
                    continue
                elif d < b:
                    ns.append(None)
                    seeds.append([d, b - d])
                    seeds[i][0] = b
                    seeds[i][1] -= b - d
                ns[i] = [(a - b) + max(d, b), min(d + e, b + c) - max(d, b)]
                if d + e > b + c:
                    ns.append(None)
                    seeds.append([b + c, d + e - b - c])
                    seeds[i][1] -= (d + e) - (b + c)
            for i, x in enumerate(ns):
                if x is None:
                    ns[i] = seeds[i]
        seeds = ns

    print(min(seed for seed, _ in seeds))