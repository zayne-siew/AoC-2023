from collections import Counter

s = '23456789TJQKA'

with open('d7p1.txt') as f:
    hands = [x.strip().split() for x in f.readlines()]
    hands.sort(key=lambda t: (sorted(Counter(t[0]).values(), reverse=True), [s.index(ch) for ch in t[0]]))
    print(hands)
    print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(hands)))