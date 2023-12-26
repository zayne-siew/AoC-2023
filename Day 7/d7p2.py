from collections import Counter

s = 'J23456789TQKA'

with open('d7p1.txt') as f:
    hands = [list(x.strip().split()) for x in f.readlines()]
    for i, (hand, bid) in enumerate(hands):
        c = Counter(hand)
        if hand != 'JJJJJ' and 'J' in c:
            x = c.pop('J')
            c[c.most_common(1)[0][0]] += x
        hands[i] = [sorted(c.values(), reverse=True), [s.index(ch) for ch in hand], int(bid)]
    hands.sort()
    print(sum((i + 1) * bid for i, (_, _, bid) in enumerate(hands)))