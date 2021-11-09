import sys

f = open(sys.argv[1])
cups1 = list(map(int, list(f.read().strip())))
cups2 = cups1.copy()

for i in range(100):
    current_cup = cups1[0]
    pick_up = cups1[1:4]
    destination = max(cups1) if current_cup - 1 < 1 else current_cup - 1
    while destination in pick_up:
        destination -= 1
        if destination < min(cups1):
            destination = max(cups1)
    destination_index = cups1.index(destination)
    tmp = []
    if destination_index == 4:
        tmp.append(destination)
        tmp += pick_up
        tmp += cups1[5:]
        tmp.append(current_cup)
        cups1 = tmp
    else:
        tmp += cups1[4:destination_index + 1]
        tmp += pick_up
        tmp += cups1[destination_index + 1:]
        tmp.append(current_cup)
        cups1 = tmp

solution1 = ''
index_one = cups1.index(1)
solution1 = solution1.join(
    list(map(str, cups1[index_one + 1:] + cups1[:index_one])))

print(f'Part 1: {solution1}')

current_cup = cups2[0]
successors = [0] * 10
for i in range(8):
    successors[cups2[i]] = cups2[i+1]
successors.extend(range(11, 1000002))
successors[cups2[-1]] = 10
successors[1000000] = current_cup

for _ in range(10000000):
    cup0 = successors[current_cup]
    cup1 = successors[cup0]
    cup2 = successors[cup1]
    next_cup = successors[cup2]

    destination = max(successors) if current_cup - 1 < 1 else current_cup - 1
    while destination in [cup0, cup1, cup2]:
        destination -= 1
        if destination < 1:
            destination = max(successors)

    successors[current_cup] = next_cup
    successors[cup2] = successors[destination]
    successors[destination] = cup0
    current_cup = next_cup

solution2 = successors[1] * successors[successors[1]]
print(f'Part 2: {solution2}')
