import sys

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')
player1, player2 = [x[9:].split() for x in data]

player1 = list(map(int, player1))
player2 = list(map(int, player2))


def combat(player1, player2):
    while player1 and player2:
        if player1[0] > player2[0]:
            tmp = player1[1:]
            tmp.append(player1[0])
            player1 = tmp
            player1.append(player2[0])
            player2 = player2[1:]
        else:
            tmp = player2[1:]
            tmp.append(player2[0])
            player2 = tmp
            player2.append(player1[0])
            player1 = player1[1:]

    return player1 if len(player1) > len(player2) else player2


solution1 = 0
winner = combat(player1, player2)
length = len(winner)
for x in winner:
    solution1 += x * length
    length -= 1

print(f'Part 1: {solution1}')


def recursive_combat(player1, player2):
    memory = []

    while player1 and player2:
        if (str(player1), str(player2)) in memory:
            tmp = player1[1:]
            tmp.append(player1[0])
            player1 = tmp
            player1.append(player2[0])
            player2 = player2[1:]

            return (1, player1)
        else:
            memory.append((str(player1), str(player2)))

            if player1[0] <= len(player1[1:]) and player2[0] <= len(
                    player2[1:]):
                winner, _ = recursive_combat(player1[1:player1[0] + 1].copy(),
                                             player2[1:player2[0] + 1].copy())
                if winner == 1:
                    tmp = player1[1:]
                    tmp.append(player1[0])
                    player1 = tmp
                    player1.append(player2[0])
                    player2 = player2[1:]
                else:
                    tmp = player2[1:]
                    tmp.append(player2[0])
                    player2 = tmp
                    player2.append(player1[0])
                    player1 = player1[1:]
            elif player1[0] > player2[0]:
                tmp = player1[1:]
                tmp.append(player1[0])
                player1 = tmp
                player1.append(player2[0])
                player2 = player2[1:]
            else:
                tmp = player2[1:]
                tmp.append(player2[0])
                player2 = tmp
                player2.append(player1[0])
                player1 = player1[1:]

    return (1, player1) if len(player1) > len(player2) else (2, player2)


solution2 = 0
_, winner = recursive_combat(player1, player2)
length = len(winner)
for x in winner:
    solution2 += x * length
    length -= 1

print(f'Part 2: {solution2}')
