import sys

f = open(sys.argv[1])
data = f.read().strip().split()
data = [int(d) for d in data]

preamble = 25

for k in range(preamble, len(data)):
    passed = False
    for i in range(k - preamble, k):
        for j in range(k - preamble, k):
            if data[i] <= data[k] and data[j] <= data[k]:
                if i != j and data[i] + data[j] == data[k]:
                    passed = True
                    break
        if passed:
            break

    if not passed:
        part1 = data[k]
        break

found = False
for i in range(len(data)):
    for j in range(i + 2, len(data)):
        if sum(data[i:j]) == part1:
            part2 = min(data[i:j]) + max(data[i:j])
            found = True
            break
        elif sum(data[i:j]) >= part1:
            break
    if found:
        break

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
