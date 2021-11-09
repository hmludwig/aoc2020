import re
import sys

f = open(sys.argv[1])
data = f.read().strip().split()

mask = None
memory1 = dict()
memory2 = dict()

for i in range(len(data)):
    if data[i] == 'mask':
        mask = data[i + 2]
    elif data[i].startswith('mem'):
        key = data[i]
        key = int(re.sub('\D+', '', key))

        value = int(format(int(data[i + 2]), '036b'), 2)

        value1 = value
        value1 &= int(mask.replace('X', '1'), 2)
        value1 |= int(mask.replace('X', '0'), 2)

        memory1[key] = value

        key |= int(mask.replace('X', '0'), 2)
        key = list(format(key, '036b'))
        for i in range(len(key)):
            if mask[i] == 'X':
                key[i] = 'X'

        keys = list()
        x_count = key.count('X')
        x_max = int('1' * x_count, 2)
        for j in range(x_max + 1):
            xs = list(format(j, '0' + str(x_count) + 'b'))
            tmp = ''
            m = 0
            for k in range(len(key)):
                if key[k] == 'X':
                    tmp += xs[m]
                    m += 1
                else:
                    tmp += key[k]
            keys.append(tmp)

        for key in keys:
            memory2[key] = value

sum1 = 0
for key in memory1:
    sum1 += memory1[key]

sum2 = 0
for key in memory2:
    sum2 += memory2[key]

print(f'Part 1: {sum1}')
print(f'Part 2: {sum2}')
