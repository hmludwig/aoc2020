import sys


def check_bag(bags, contents):
    for bag in contents:
        if bag == 'no_other':
            continue
        elif bag == 'shiny_gold':
            return True
        else:
            if check_bag(bags, bags[bag]):
                return True
            else:
                continue
    return False


def count_bags(bags, contents):
    cnt = 0
    for bag in contents:
        if bag == 'no_other':
            continue
        else:
            cnt += 1
            cnt += count_bags(bags, bags[bag])

    return cnt


f = open(sys.argv[1])
data = f.read().strip().split('\n')

bags1 = dict()
bags2 = dict()

for d in data:
    words = d.replace(',', '').replace('.', '').split()
    key = words[0] + '_' + words[1]
    bags1[key] = []
    bags2[key] = []
    for i in range(4, len(words)):
        if words[i] == 'bag' or words[i] == 'bags':
            name = words[i - 2] + '_' + words[i - 1]
            bags1[key].append(name)

            if name != 'no_other':
                for j in range(0, int(words[i - 3])):
                    bags2[key].append(words[i - 2] + '_' + words[i - 1])

cnt1 = 0
cnt2 = 0

for bag in bags1:
    if check_bag(bags1, bags1[bag]):
        cnt1 += 1

cnt2 += count_bags(bags2, bags2['shiny_gold'])

print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')
