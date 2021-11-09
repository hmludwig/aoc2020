import sys
import numpy as np

f = open(sys.argv[1])
data = f.read().strip().split()


def make_move1(move, amount, x, y):
    if move == 'N':
        y += amount
    elif move == 'S':
        y -= amount
    elif move == 'E':
        x += amount
    elif move == 'W':
        x -= amount

    return (x, y)


def make_move2(move, amount, x, y, wx, wy):
    if move == 'F':
        y += amount * wy
        x += amount * wx
    elif move == 'N':
        wy += amount
    elif move == 'S':
        wy -= amount
    elif move == 'E':
        wx += amount
    elif move == 'W':
        wx -= amount

    return (x, y, wx, wy)


x = 0
y = 0
directions = np.array(['E', 'S', 'W', 'N'])
for d in data:
    move = d[0]
    amount = int(d[1:])
    if move == 'F':
        x, y = make_move1(directions[0], amount, x, y)
    elif move == 'R':
        t = amount // 90
        directions = np.roll(directions, -t)
    elif move == 'L':
        t = amount // 90
        directions = np.roll(directions, t)
    else:
        x, y = make_move1(move, amount, x, y)

print(f'Part 1: {abs(x) + abs(y)}')

x = 0
y = 0
wx = 10
wy = 1
for d in data:
    move = d[0]
    amount = int(d[1:])
    if move == 'F':
        x, y, wx, wy = make_move2('F', amount, x, y, wx, wy)
    elif move == 'R':
        t = amount // 90
        for _ in range(t):
            wx, wy = wy, -wx
    elif move == 'L':
        t = amount // 90
        for _ in range(t):
            wx, wy = -wy, wx
    else:
        x, y, wx, wy = make_move2(move, amount, x, y, wx, wy)

print(f'Part 2: {abs(x) + abs(y)}')
