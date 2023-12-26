def hf(s):
    res = 0
    for ch in s:
        res = ((res + ord(ch)) * 17) % 256
    return res

with open('d15p1.txt') as f:
    print(sum(hf(line) for line in f.read().strip().split(',')))