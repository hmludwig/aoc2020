import sys

f = open(sys.argv[1])
data = f.read().strip().split(',')
data = [int(d) for d in data]


def calculate(nums, n):
    i = 0
    prev = nums[-1]
    numbers = dict()
    numbers[0] = list()
    while i < n:
        if i < len(nums):
            numbers[nums[i]] = [i]
            i += 1
        else:
            if len(numbers[prev]) == 1:
                numbers[0].append(i)
                prev = 0
            else:
                prev = numbers[prev][-1] - numbers[prev][-2]
                if prev in numbers:
                    numbers[prev].append(i)
                else:
                    numbers[prev] = [i]
            i += 1

    return prev


print(f'Part 1: {calculate(data, 2020)}')
print(f'Part 2: {calculate(data, 30000000)}')
