import collections
import math

start = 'broadcaster'

def parse(inp):
    mods = dict()
    cables = dict()

    for line in inp.splitlines():
        mod, outs = line.split(' -> ')
        if mod[0] in '%&':
            op, mod = mod[0], mod[1:]
            mods[mod] = op
        cables[mod] = outs.split(', ')
    return mods, cables


def init_mem(mods, cables):
    mem = dict()
    for mod, op in mods.items():
        match op:
            case '%':
                mem[mod] = False
            case '&':
                mem[mod] = dict()

    for mod, outs in cables.items():
        for out in outs:
            if mods.get(out) == '&':
                mem[out][mod] = False

    return mem


def press_button(mods, cables, mem, cnt):
    # Initial low pulse
    cnt[0] += 1

    queue = collections.deque()
    for out in cables[start]:
        queue.append((start, out, False))

    while queue:
        src, dst, pulse = queue.popleft()
        cnt[pulse] += 1

        match mods.get(dst):
            case '%':
                if not pulse:
                    mem[dst] = not mem[dst]
                    for out in cables[dst]:
                        queue.append((dst, out, mem[dst]))

            case '&':
                mem[dst][src] = pulse
                pulse = not all(mem[dst].values())
                for out in cables[dst]:
                    queue.append((dst, out, pulse))


def count(gate, mods, cables):
    # Counter works by sending a signal through a flip-flop chain. A flip-flop
    # that sends a signal to the reset/ouput gate counts as a HI digit in the
    # cycle count.
    cnt = 0
    pos  = 1
    while True:
        outs = cables[gate]
        if len(outs) == 2:
            a, b = outs
            gate = a if mods[a] == '%' else b
            cnt += pos
        else:
            a = outs[0]
            if mods[a] == '%':
                gate = a
            else:
                cnt += pos
                break
        pos *= 2
    return cnt


def part2(machine):
    # This works for my input, but not necessarily for yours.

    # Unfortunately, a general solution would be to difficult to implement.
    # We must exploit the structure of the input. Broadcaster feeds into
    # 4 binary counters, which themselves feed into a common comperator.
    mods, cables = machine
    cnts = [count(gate, mods, cables) for gate in cables[start]]

    # Comperator is only active when all cycles line up
    return math.lcm(*cnts)

print(part2(parse(open('d20p1.txt').read().strip())))