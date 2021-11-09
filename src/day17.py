import sys
import numpy as np

N_CYCLES = 6

f = open(sys.argv[1])
data = f.read().strip().splitlines()

world1 = np.zeros((1, len(data), len(data[0])), dtype=int)
world2 = np.zeros((1, 1, len(data), len(data[0])), dtype=int)

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            world1[0][i][j] = 1
            world2[0][0][i][j] = 1

for i in range(N_CYCLES + 1):
    world1 = np.pad(world1, 1, 'constant', constant_values=0)
    world2 = np.pad(world2, 1, 'constant', constant_values=0)

for _ in range(N_CYCLES):
    shape = world1.shape
    tmp = np.zeros(shape, dtype=int)
    for i in range(0, shape[0] - 2):
        for j in range(0, shape[1] - 2):
            for k in range(0, shape[2] - 2):
                x = world1[i:i + 3, j:j + 3, k:k + 3]
                center = x[1][1][1]
                if center == 1 and (x.sum() - 1 < 2 or x.sum() - 1 > 3):
                    tmp[i + 1][j + 1][k + 1] = 0
                elif center == 1:
                    tmp[i + 1][j + 1][k + 1] = 1
                elif center == 0 and x.sum() == 3:
                    tmp[i + 1][j + 1][k + 1] = 1
                x[1][1][1] = center
    world1 = tmp

for _ in range(N_CYCLES):
    shape = world2.shape
    tmp = np.zeros(shape, dtype=int)
    for i in range(0, shape[0] - 2):
        for j in range(0, shape[1] - 2):
            for k in range(0, shape[2] - 2):
                for l in range(0, shape[3] - 2):
                    x = world2[i:i + 3, j:j + 3, k:k + 3, l:l + 3]
                    center = x[1][1][1][1]
                    if center == 1 and (x.sum() - 1 < 2 or x.sum() - 1 > 3):
                        tmp[i + 1][j + 1][k + 1][l + 1] = 0
                    elif center == 1:
                        tmp[i + 1][j + 1][k + 1][l + 1] = 1
                    elif center == 0 and x.sum() == 3:
                        tmp[i + 1][j + 1][k + 1][l + 1] = 1
    world2 = tmp

print(f'Part 1: {world1.sum()}')
print(f'Part 2: {world2.sum()}')
