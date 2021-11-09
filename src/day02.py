import sys

f = open(sys.argv[1])
data = f.read().split()

count1 = 0
count2 = 0

for i in range(0, len(data), 3):
    cminmax = data[i].split('-')
    cmin = int(cminmax[0])
    cmax = int(cminmax[1])
    csearch = data[i + 1][0]
    password = data[i + 2]
    if cmin <= password.count(csearch) <= cmax:
        count1 += 1
    if (password[cmin - 1] == csearch) != (password[cmax - 1] == csearch):
        count2 += 1

print(f'Part 1: {count1}')
print(f'Part 2: {count2}')
