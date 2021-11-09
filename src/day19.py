import sys

f = open(sys.argv[1])
rules, messages = f.read().strip().split('\n\n')
rules = rules.splitlines()
messages = messages.splitlines()

rule_dict1 = {}
rule_dict2 = {}
for r in rules:
    rule_nr, rule = r.split(': ')
    rule_dict1[int(rule_nr)] = rule
    rule_dict2[int(rule_nr)] = rule

rule_dict2[8] = '42 | 42 8'
rule_dict2[11] = '42 31 | 42 11 31'


def consume_message(message, rule_dict, rule_number):
    rule = rule_dict[rule_number]
    if rule[0] == '"':
        rule = rule.strip('"')
        if message.startswith(rule):
            return [len(rule)]
        else:
            return []

    all_amounts = []
    for r in rule.split(' | '):
        acc = [0]
        for rule_number in r.split(' '):
            rule_number = int(rule_number)
            tmp = []
            for ac in acc:
                amounts = consume_message(message[ac:], rule_dict, rule_number)
                for a in amounts:
                    tmp.append(ac + a)
            acc = tmp
        all_amounts += acc

    return all_amounts


solution1 = 0
solution2 = 0
for message in messages:
    if len(message) in consume_message(message, rule_dict1, 0):
        solution1 += 1
    if len(message) in consume_message(message, rule_dict2, 0):
        solution2 += 1

print(f'Part 1: {solution1}')
print(f'Part 2: {solution2}')
