import sys
import numpy as np


class Tile:

    def __init__(self, tile_id, tile):
        self.tile_id = tile_id
        self.tile = tile

    def __str__(self):
        tile_string = ''
        for i in range(len(self.tile)):
            tile_string += '\n'
            for j in range(len(self.tile)):
                tile_string += self.tile[i][j]
        return tile_string

    def rotations(self):
        for _ in range(2):
            for _ in range(4):
                yield self
                self.tile = np.rot90(self.tile)
            self.tile = np.flip(self.tile, 0)


class Image:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.image = np.zeros((height, width), dtype=object)
        for i in range(height):
            for j in range(width):
                self.image[i][j] = Tile(-1, None)

    def __str__(self):
        rows = []
        for i in range(self.height):
            row = []
            for j in range(self.height):
                if self.image[i][j].tile_id != -1:
                    row.append(self.image[i][j].tile)
                else:
                    row.append(np.zeros((10, 10), dtype=str))
            rows.append(np.concatenate(row, axis=1))
        tmp = np.concatenate(rows, axis=0)

        image_string = ''
        for i in range(len(tmp)):
            image_string += '\n'
            for j in range(len(tmp[0])):
                image_string += tmp[i][j]
        return image_string

    def valid_image(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.image[i][j].tile_id == -1:
                    return False
                elif not check_image(self, i, j):
                    return False
        return True

    def print_ids(self):
        for i in range(self.height):
            print()
            for j in range(self.width):
                print(self.image[i][j].tile_id, end=' ')
        print()

def rotations(x):
    for _ in range(2):
        for _ in range(4):
            yield x
            x = np.rot90(x)
        x = np.flip(x, 0)


def check_tile_above(image, i, j):
    if image.image[i - 1][j].tile_id != -1:
        if np.all(
                image.image[i -
                            1][j].tile[-1, :] == image.image[i][j].tile[0, :]):
            return True
        else:
            return False
    else:
        return True


def check_tile_below(image, i, j):
    if image.image[i + 1][j].tile_id != -1:
        if np.all(
                image.image[i +
                            1][j].tile[0, :] == image.image[i][j].tile[-1, :]):
            return True
        else:
            return False
    else:
        return True


def check_tile_left(image, i, j):
    if image.image[i][j - 1].tile_id != -1:
        if np.all(image.image[i][j - 1].tile[:,
                                             -1] == image.image[i][j].tile[:,
                                                                           0]):
            return True
        else:
            return False
    else:
        return True


def check_tile_right(image, i, j):
    if image.image[i][j + 1].tile_id != -1:
        if np.all(image.image[i][j + 1].tile[:,
                                             0] == image.image[i][j].tile[:,
                                                                          -1]):
            return True
        else:
            return False
    else:
        return True


def check_image(image, i, j):
    checks = []
    # Left upper corner
    if i == 0 and j == 0:
        checks.append(check_tile_right(image, i, j))
        checks.append(check_tile_below(image, i, j))
    # Right upper corner
    elif i == 0 and j == size - 1:
        checks.append(check_tile_left(image, i, j))
        checks.append(check_tile_below(image, i, j))
    # Left bottom corner
    elif i == size - 1 and j == 0:
        checks.append(check_tile_right(image, i, j))
        checks.append(check_tile_above(image, i, j))
    # Right bottom corner
    elif i == size - 1 and j == size - 1:
        checks.append(check_tile_left(image, i, j))
        checks.append(check_tile_above(image, i, j))
    # Top edge
    elif i == 0:
        checks.append(check_tile_left(image, i, j))
        checks.append(check_tile_right(image, i, j))
        checks.append(check_tile_below(image, i, j))
    # Bottom edge
    elif i == size - 1:
        checks.append(check_tile_left(image, i, j))
        checks.append(check_tile_right(image, i, j))
        checks.append(check_tile_above(image, i, j))
    # Left edge
    elif j == 0:
        checks.append(check_tile_above(image, i, j))
        checks.append(check_tile_right(image, i, j))
        checks.append(check_tile_below(image, i, j))
    # Right edge
    elif j == size - 1:
        checks.append(check_tile_left(image, i, j))
        checks.append(check_tile_above(image, i, j))
        checks.append(check_tile_below(image, i, j))
    # Middle tile
    else:
        checks.append(check_tile_left(image, i, j))
        checks.append(check_tile_above(image, i, j))
        checks.append(check_tile_below(image, i, j))
        checks.append(check_tile_right(image, i, j))

    if all(checks):
        return True
    else:
        return False


def make_image(image, tiles, i, j):
    if i == image.height:
        return True
    for tile in tiles:
        for t in tile.rotations():
            image.image[i][j] = t
            if not check_image(image, i, j):
                image.image[i][j] = Tile(-1, None)
                continue

            if j == image.width - 1:
                tmp = [x for x in tiles if x != t]
                if make_image(image, tmp, i + 1, 0):
                    return True
            else:
                tmp = [x for x in tiles if x != t]
                if make_image(image, tmp, i, j + 1):
                    return True
            image.image[i][j] = Tile(-1, None)
    return False


if __name__ == '__main__':
    f = open(sys.argv[1])
    data = f.read().strip().split('\n\n')

    tiles = []
    for d in data:
        d = d.splitlines()
        tile_id = d[0].split(' ')
        tile_id = int(tile_id[1].strip(':'))

        tmp = []
        for i in range(1, len(d)):
            tmp.append(list(d[i]))
        tiles.append(Tile(tile_id, np.array(tmp)))

    size = int(np.sqrt(len(tiles)))
    image = Image(size, size)
    make_image(image, tiles, 0, 0)

    solution1 = image.image[0][0].tile_id * image.image[0][
        -1].tile_id * image.image[-1][0].tile_id * image.image[-1][-1].tile_id

    print(f'Part 1: {solution1}')

    sea_monster = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
    sea_monster = [x.replace(' ', '0').replace('#', '1') for x in sea_monster]
    sea_monster = [[c for c in x] for x in sea_monster]
    sea_monster = np.array(sea_monster, dtype=int)
    n_ones = sum(sum(sea_monster))

    for i in range(image.height):
        for j in range(image.width):
            image.image[i][j].tile = image.image[i][j].tile[1:-1, 1:-1]

    image_string = image.__str__().replace('.', '0').replace('#','1').split()
    image_string = [[c for c in x] for x in image_string]
    image_string = np.array(image_string, dtype=int)

    n_sea_monsters = 0
    m, n = sea_monster.shape
    for x in rotations(image_string):
        for i in range(len(image_string) - m + 1):
            for j in range(len(image_string) - n + 1):
                if np.sum(x[i:i+m, j:j+n] * sea_monster) == n_ones:
                    n_sea_monsters += 1
        if n_sea_monsters != 0:
            break

    solution2 = sum(sum(image_string)) - n_sea_monsters * n_ones
    print(f'Part 2: {solution2}')
