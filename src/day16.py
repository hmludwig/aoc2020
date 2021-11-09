import sys
from collections import defaultdict
import numpy as np

f = open(sys.argv[1])
data = f.read().strip().splitlines()
data = [d for d in data if d.strip() != '']
rules = dict()
rules_section = True
my_ticket = None
tickets = list()
departure_rules = list()

for i, d in enumerate(data):
    if d == 'your ticket:':
        rules_section = False
        my_ticket = [int(x) for x in data[i + 1].split(',')]
    elif d == 'nearby tickets:':
        for k in range(i + 1, len(data)):
            tickets.append([int(x) for x in data[k].split(',')])
        break
    elif rules_section:
        tmp = d.split(': ')
        rule_name = tmp[0]
        if 'departure' in rule_name:
            departure_rules.append(rule_name)
        rule_range = [x.split('-') for x in tmp[1].split(' or ')]
        rules[rule_name] = [(int(x[0]), int(x[1])) for x in rule_range]

error_rate = 0
invalid = list()

for i in range(len(tickets)):
    for j in tickets[i]:
        valid = False
        for m in rules:
            for n in rules[m]:
                if j >= n[0] and j <= n[1]:
                    valid = True
                    break
        if not valid:
            invalid.append(tickets[i])
            error_rate += j

print(f'Part 1: {error_rate}')


def check_rule_at_pos(ticket, rule, pos):
    if (ticket[pos] >= rule[0][0] and
            ticket[pos] <= rule[0][1]) or (ticket[pos] >= rule[1][0] and
                                           ticket[pos] <= rule[1][1]):
        return True
    return False


rule_index = defaultdict(list)

for r in rules:
    rule = rules[r]
    for pos in range(len(my_ticket)):
        good_pos = True
        for ticket in tickets:
            if ticket not in invalid:
                if not check_rule_at_pos(ticket, rule, pos):
                    good_pos = False
                    break
        if good_pos:
            rule_index[r].append(pos)

table = list()
for i, k in enumerate(rule_index):
    table.append([])
    for j in range(len(my_ticket)):
        if j in rule_index[k]:
            table[i].append(1)
        else:
            table[i].append(0)

positions = list()
table = np.array(table)

while len(positions) != 6:
    for i in range(len(my_ticket)):
        if sum(table[:, i]) == 1:
            for j, x in enumerate(table[:, i]):
                if x == 1:
                    if j < 6:
                        positions.append(i)
                    table[j, :] = 0

prod = 1
for x in positions:
    prod *= my_ticket[x]

print(f'Part 2: {prod}')
