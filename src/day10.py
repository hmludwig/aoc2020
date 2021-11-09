import sys
from collections import defaultdict

f = open(sys.argv[1])
data = f.read().strip().split()
data = sorted([int(d) for d in data])

charging_outlet = max(data) + 3
data = [0] + data + [charging_outlet]

cnt_diff1 = 0
cnt_diff3 = 0
for i in range(len(data) - 1):
    if data[i + 1] - data[i] == 1:
        cnt_diff1 += 1
    elif data[i + 1] - data[i] == 3:
        cnt_diff3 += 1

branches = defaultdict(int)
device = data.pop()
branches[device] = 1
for i in reversed(data):
    branches[i] = branches[i + 1] + branches[i + 2] + branches[i + 3]

print(f'Part 1: {cnt_diff1 * cnt_diff3}')
print(f'Part 2: {branches[0]}')
