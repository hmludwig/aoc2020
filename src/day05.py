import sys

f = open(sys.argv[1])
data = f.read().split()

seat_ids = []

for d in data:
    binary_row = d[0:7].replace('F', '0').replace('B', '1')
    binary_column = d[7:].replace('L', '0').replace('R', '1')
    row = int(binary_row, 2)
    column = int(binary_column, 2)
    seat_ids.append(row * 8 + column)

my_seat_id = [
    i for i in range(min(seat_ids), max(seat_ids))
    if i not in seat_ids and (i + 1) in seat_ids and (i - 1) in seat_ids
][0]

print(f'Part 1: {max(seat_ids)}')
print(f'Part 2: {my_seat_id}')
