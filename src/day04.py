import sys
import json
import re

f = open(sys.argv[1])
data = f.read().split('\n\n')
data = [x.strip('\n').replace('\n', ' ') for x in data]

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

cnt1 = 0
cnt2 = 0

for d in data:
    passport = '{"' + d.replace(':', '":"').replace(' ', '", "') + '"}'
    passport = json.loads(passport)
    if all(i in passport for i in required_fields):
        cnt1 += 1
        check_sum = 0
        for x in passport:
            if x == 'byr':
                if 1920 <= int(passport[x]) <= 2002:
                    check_sum += 1
            if x == 'iyr':
                if 2010 <= int(passport[x]) <= 2020:
                    check_sum += 1
            if x == 'eyr':
                if 2020 <= int(passport[x]) <= 2030:
                    check_sum += 1
            if x == 'hgt':
                tmp = passport[x].replace('i', ' i').replace('c', ' c').split()
                if len(tmp) == 2:
                    if tmp[1] == 'in':
                        if 59 <= int(tmp[0]) <= 76:
                            check_sum += 1
                    else:
                        if 150 <= int(tmp[0]) <= 193:
                            check_sum += 1
            if x == 'hcl':
                prog = re.compile('([0-9]|[a-f])*$')
                if passport[x][0] == '#' and prog.match(passport[x][1:]):
                    check_sum += 1
            if x == 'ecl':
                if any(i in passport[x] for i in eye_colors):
                    check_sum += 1
            if x == 'pid':
                if len(passport[x]) == 9:
                    check_sum += 1

        if check_sum == 7:
            cnt2 += 1

print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')
