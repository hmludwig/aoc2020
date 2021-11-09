import sys

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')
data1 = [d.replace('\n', '') for d in data]
data2 = [d.split('\n') for d in data]

part1 = 0
part2 = 0

for d in data1:
    part1 += len(set(d))

for d in data2:
    d_set = [set(d[i]) for i in range(len(d))]
    part2 += len(set.intersection(*d_set))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
