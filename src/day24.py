import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()


def parse_hex_directions(direction):
    directions = []
    i = 0
    while i < len(direction):
        if direction[i] in ['e', 'w']:
            directions.append(direction[i])
            i += 1
        elif direction[i] in ['s', 'n']:
            directions.append(direction[i:i + 2])
            i += 2
    return directions


def direction2coordinate(direction):
    if direction == 'e':
        return (1, 0)
    elif direction == 'se':
        return (0.5, 0.5)
    elif direction == 'sw':
        return (-0.5, 0.5)
    elif direction == 'w':
        return (-1, 0)
    elif direction == 'nw':
        return (-0.5, -0.5)
    elif direction == 'ne':
        return (0.5, -0.5)
    else:
        return (0, 0)


def check_adjacent_tiles(tiles, key):
    adjacent_tiles = []
    n_black_tiles = 0
    adjacent_tiles.append((1 + key[0], 0 + key[1]))
    adjacent_tiles.append((0.5 + key[0], 0.5 + key[1]))
    adjacent_tiles.append((-0.5 + key[0], 0.5 + key[1]))
    adjacent_tiles.append((-1 + key[0], 0 + key[1]))
    adjacent_tiles.append((-0.5 + key[0], -0.5 + key[1]))
    adjacent_tiles.append((0.5 + key[0], -0.5 + key[1]))

    for tile in adjacent_tiles:
        if tile in tiles:
            n_black_tiles += tiles[tile]

    return n_black_tiles


black_tiles = []

for d in data:
    directions = parse_hex_directions(d)
    posx = 0
    posy = 0
    for direction in directions:
        x, y = direction2coordinate(direction)
        posx += x
        posy += y
    if (posx, posy) in black_tiles:
        black_tiles.remove((posx, posy))
    else:
        black_tiles.append((posx, posy))

solution1 = len(black_tiles)
print(f'Part 1: {solution1}')

tiles = {}
x = -100
y = -100
for _ in range(400):
    x += 0.5
    y = -100
    for _ in range(400):
        tiles[(x, y)] = 0
        y += 0.5

for tile in black_tiles:
    tiles[tile] = 1

for _ in range(100):
    tmp = tiles.copy()
    for key in tiles:
        black_adjacent_tiles = check_adjacent_tiles(tiles, key)
        if tiles[key] == 0 and black_adjacent_tiles == 2:
            tmp[key] = 1
        elif tiles[key] == 1 and (black_adjacent_tiles == 0 or
                                  black_adjacent_tiles > 2):
            tmp[key] = 0
    tiles = tmp

solution2 = sum([tiles[k] for k in tiles])
print(f'Part 2: {solution2}')
