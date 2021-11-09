import sys

f = open(sys.argv[1])
data = f.read().strip().split()


def run_programm(programm, line=-1):
    if line != -1:
        if programm[line] == 'nop':
            programm[line] = 'jmp'
        elif programm[line] == 'jmp':
            programm[line] = 'nop'
        else:
            print('ERROR: WRONG LINE')
    acc = 0
    visited_lines = []

    i = 0
    while True:
        if i in visited_lines:
            terminated = False
            break
        elif i == len(programm):
            terminated = True
            break
        elif programm[i] == 'nop':
            visited_lines.append(i)
            i += 2
        elif programm[i] == 'acc':
            visited_lines.append(i)
            acc = eval('acc' + programm[i + 1])
            i += 2
        else:
            visited_lines.append(i)
            factor = eval('0' + programm[i + 1])
            i += 2 * factor

    return (terminated, acc)


terminated, acc = run_programm(data.copy())
print(f'Part 1: {acc}')

j = 0
while True:
    if terminated:
        break
    else:
        while data[j] not in ['nop', 'jmp']:
            j += 1
        terminated, acc = run_programm(data.copy(), j)
        j += 1

print(f'Part 2: {acc}')
