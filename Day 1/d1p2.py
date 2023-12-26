nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero')

with open('d1p1.txt', 'r') as f:
    total = 0
    for line in f.read().split('\n'):
        a = min(nums, key=lambda num: i if (i := line.find(num)) >= 0 else float('inf'))
        b = max(nums, key=lambda num: line.rfind(num))
        total += (nums.index(a) % 10 + 1) * 10 + (nums.index(b) % 10 + 1)
    print(total)