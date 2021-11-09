import sys
import math

f = open(sys.argv[1])
data = f.read().strip().split()

earliest_timestamp = int(data[0])
lines = [(int(d), i) for i, d in enumerate(data[1].split(',')) if d != 'x']

times = [(line, line - (earliest_timestamp % line)) for line, _ in lines]

change_rate = 1
timestamp = 0
for line, dt in lines:
    while True:
        if (dt + timestamp) % line == 0:
            break
        timestamp += change_rate
    change_rate *= line

print(f'Part 1: {math.prod(min(times, key= lambda x: x[1]))}')
print(f'Part 2: {timestamp}')
