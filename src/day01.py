import sys

f = open(sys.argv[1])
data = f.read().split()
data = [int(i) for i in data]
data.sort()

no_solution1 = True
no_solution2 = True

for i, m in enumerate(data):
    for j, n in enumerate(data):
        for k, o in enumerate(data):
            if not no_solution1 and not no_solution2:
                break
            if i != j and i != k and j != k:
                if no_solution1 and m + n == 2020:
                    print(f"Solution 1: {m * n}")
                    no_solution1 = False
                if no_solution2 and m + n + o == 2020:
                    print(f"Solution 2: {m * n * o}")
                    no_solution2 = False
