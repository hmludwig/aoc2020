import sys
import copy

f = open(sys.argv[1])
data = f.read().strip().split()
data = [list(d) for d in data]


def print_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end='')
        print()
    print()


def game_of_seats1(state):
    tmp = copy.deepcopy(state)
    changed = False
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '.':
                continue

            cnt = 0
            if i == 0 and j == 0:
                if state[i][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j] == '#':
                    cnt += 1
            elif i == 0 and j == len(state[i]) - 1:
                if state[i + 1][j] == '#':
                    cnt += 1
                if state[i + 1][j - 1] == '#':
                    cnt += 1
                if state[i][j - 1] == '#':
                    cnt += 1
            elif i == 0:
                if state[i][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j] == '#':
                    cnt += 1
                if state[i + 1][j - 1] == '#':
                    cnt += 1
                if state[i][j - 1] == '#':
                    cnt += 1
            elif i == len(state) - 1 and j == 0:
                if state[i][j + 1] == '#':
                    cnt += 1
                if state[i - 1][j] == '#':
                    cnt += 1
                if state[i - 1][j + 1] == '#':
                    cnt += 1
            elif j == 0:
                if state[i][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j] == '#':
                    cnt += 1
                if state[i - 1][j] == '#':
                    cnt += 1
                if state[i - 1][j + 1] == '#':
                    cnt += 1
            elif i == len(state) - 1 and j == len(state[i]) - 1:
                if state[i][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j] == '#':
                    cnt += 1
            elif i == len(state) - 1:
                if state[i][j + 1] == '#':
                    cnt += 1
                if state[i][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j] == '#':
                    cnt += 1
                if state[i - 1][j + 1] == '#':
                    cnt += 1
            elif j == len(state[i]) - 1:
                if state[i + 1][j] == '#':
                    cnt += 1
                if state[i + 1][j - 1] == '#':
                    cnt += 1
                if state[i][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j] == '#':
                    cnt += 1
            else:
                if state[i][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j + 1] == '#':
                    cnt += 1
                if state[i + 1][j] == '#':
                    cnt += 1
                if state[i + 1][j - 1] == '#':
                    cnt += 1
                if state[i][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j - 1] == '#':
                    cnt += 1
                if state[i - 1][j] == '#':
                    cnt += 1
                if state[i - 1][j + 1] == '#':
                    cnt += 1

            if state[i][j] == 'L' and cnt == 0:
                tmp[i][j] = '#'
                changed = True
            elif state[i][j] == '#' and cnt >= 4:
                tmp[i][j] = 'L'
                changed = True
    return (changed, tmp)


def check_direction(state, i, j, direction):
    while 0 <= i <= len(state) - 1 and 0 <= j <= len(state[i]) - 1:
        if direction == 'n':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            i -= 1

        elif direction == 'ne':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            i -= 1
            j += 1

        elif direction == 'e':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            j += 1

        elif direction == 'se':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            i += 1
            j += 1

        elif direction == 's':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            i += 1

        elif direction == 'sw':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            i += 1
            j -= 1

        elif direction == 'w':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            j -= 1

        elif direction == 'nw':
            if state[i][j] == '#':
                return 1
            elif state[i][j] == 'L':
                return 0
            i -= 1
            j -= 1

    return 0


def game_of_seats2(state):
    tmp = copy.deepcopy(state)
    changed = False
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '.':
                continue

            cnt = 0
            if i == 0 and j == 0:
                cnt += check_direction(state, i, j + 1, 'e')
                cnt += check_direction(state, i + 1, j + 1, 'se')
                cnt += check_direction(state, i + 1, j, 's')
            elif i == 0 and j == len(state[i]) - 1:
                cnt += check_direction(state, i + 1, j, 's')
                cnt += check_direction(state, i + 1, j - 1, 'sw')
                cnt += check_direction(state, i, j - 1, 'w')
            elif i == 0:
                cnt += check_direction(state, i, j + 1, 'e')
                cnt += check_direction(state, i + 1, j + 1, 'se')
                cnt += check_direction(state, i + 1, j, 's')
                cnt += check_direction(state, i + 1, j - 1, 'sw')
                cnt += check_direction(state, i, j - 1, 'w')
            elif i == len(state) - 1 and j == 0:
                cnt += check_direction(state, i - 1, j, 'n')
                cnt += check_direction(state, i - 1, j + 1, 'ne')
                cnt += check_direction(state, i, j + 1, 'e')
            elif j == 0:
                cnt += check_direction(state, i - 1, j, 'n')
                cnt += check_direction(state, i - 1, j + 1, 'ne')
                cnt += check_direction(state, i, j + 1, 'e')
                cnt += check_direction(state, i + 1, j + 1, 'se')
                cnt += check_direction(state, i + 1, j, 's')
            elif i == len(state) - 1 and j == len(state[i]) - 1:
                cnt += check_direction(state, i, j - 1, 'w')
                cnt += check_direction(state, i - 1, j - 1, 'nw')
                cnt += check_direction(state, i - 1, j, 'n')
            elif i == len(state) - 1:
                cnt += check_direction(state, i, j - 1, 'w')
                cnt += check_direction(state, i - 1, j - 1, 'nw')
                cnt += check_direction(state, i - 1, j, 'n')
                cnt += check_direction(state, i - 1, j + 1, 'ne')
                cnt += check_direction(state, i, j + 1, 'e')
            elif j == len(state[i]) - 1:
                cnt += check_direction(state, i - 1, j, 'n')
                cnt += check_direction(state, i - 1, j - 1, 'nw')
                cnt += check_direction(state, i, j - 1, 'w')
                cnt += check_direction(state, i + 1, j - 1, 'sw')
                cnt += check_direction(state, i + 1, j, 's')
            else:
                cnt += check_direction(state, i - 1, j, 'n')
                cnt += check_direction(state, i - 1, j + 1, 'ne')
                cnt += check_direction(state, i, j + 1, 'e')
                cnt += check_direction(state, i + 1, j + 1, 'se')
                cnt += check_direction(state, i + 1, j, 's')
                cnt += check_direction(state, i + 1, j - 1, 'sw')
                cnt += check_direction(state, i, j - 1, 'w')
                cnt += check_direction(state, i - 1, j - 1, 'nw')

            if state[i][j] == 'L' and cnt == 0:
                tmp[i][j] = '#'
                changed = True
            elif state[i][j] == '#' and cnt >= 5:
                tmp[i][j] = 'L'
                changed = True
    return (changed, tmp)


changed, data1 = game_of_seats1(data)
while changed:
    changed, data1 = game_of_seats1(data1)

cnt1 = 0
for i in range(len(data1)):
    for j in range(len(data1[i])):
        if data1[i][j] == '#':
            cnt1 += 1

changed, data2 = game_of_seats2(data)
while changed:
    changed, data2 = game_of_seats2(data2)

cnt2 = 0
for i in range(len(data2)):
    for j in range(len(data2[i])):
        if data2[i][j] == '#':
            cnt2 += 1

print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')
