from collections import defaultdict, deque

d = {}
m = defaultdict(list)
for line in open('d20p1.txt').readlines():
    src, dests = line.strip().split(' -> ')
    dests = dests.split(', ')
    pre = ''
    if src[0] == '&' or src[0] == '%':
        pre, src = src[0], src[1:]
    d[src] = (pre, dests)
    for dest in dests:
        m[dest].append(src)

#print(d)
#print(m)

states = defaultdict(bool)
pulses = []
for step in range(1000):
    #print(step)
    if step and not any(states.values()):
        break
    q = deque([('broadcaster', False)])
    lo, hi = 1, 0
    while q:
        for _ in range(len(q)):
            curr, pulse = q.popleft()
            pre, dests = d.get(curr, ('', []))
            res = pulse
            if pre == '%':
                if pulse:
                    continue
                res = states[curr] = not states[curr]
            elif pre == '&':
                res = states[curr] = not all(states[prev] for prev in m[curr])
            q.extend((dest, res) for dest in dests)
            if res:
                hi += len(dests)
            else:
                lo += len(dests)
        #print(states)
    #print('final', lo, hi)
    pulses.append((lo, hi))

tot_lo = tot_hi = part_lo = part_hi = 0
quot, rmd = divmod(1000, len(pulses))
for i, (lo, hi) in enumerate(pulses):
    tot_lo += lo
    tot_hi += hi
    if rmd > i:
        part_lo += lo
        part_hi += hi

print((tot_lo * quot + part_lo) * (tot_hi * quot + part_hi))