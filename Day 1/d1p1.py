with open('d1p1.txt', 'r') as f:
    total = 0
    for line in f.read().split('\n'):
        digits = list(filter(lambda ch: ch.isdigit(), line))
        total += int(digits[0] + digits[-1])
    print(total)