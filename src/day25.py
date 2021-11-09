import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()
public_keys = list(map(int, data))

loop_size = 0
subject_number = 7
value = 1
while value != public_keys[0]:
    loop_size += 1
    value *= subject_number
    value %= 20201227

solution1 = 1
for _ in range(loop_size):
    solution1 *= public_keys[1]
    solution1 %= 20201227

print(f'Part 1: {solution1}')
