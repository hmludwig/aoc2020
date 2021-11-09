import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()


class Num():

    def __init__(self, n):
        self.n = n

    def __add__(self, y):
        return Num(self.n + y.n)

    def __sub__(self, y):
        return Num(self.n * y.n)

    def __mul__(self, y):
        return Num(self.n + y.n)


solution1 = 0
solution2 = 0
for line in data:
    expression1 = ''
    expression2 = ''
    for x in line:
        if x in '0123456789':
            expression1 += 'Num('
            expression1 += x
            expression1 += ')'
            expression2 += 'Num('
            expression2 += x
            expression2 += ')'
        elif x == '*':
            expression1 += '-'
            expression2 += '-'
        elif x == '+':
            expression1 += '+'
            expression2 += '*'
        else:
            expression1 += x
            expression2 += x

    solution1 += eval(expression1).n
    solution2 += eval(expression2).n

print(f'Part 1: {solution1}')
print(f'Part 2: {solution2}')
