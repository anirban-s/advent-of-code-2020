from collections import defaultdict

r = open("day11.txt", "r")
data = r.read().split('\n')
positions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def check_occupancy(near, rows, x, y):
    occupied = 0
    for vx, vy in positions:
        unit = 1
        dx = vx
        dy = vy
        while x + dx >= 0 and x + dx < len(rows[y]) and y + dy >= 0 and y + dy < len(rows):
            if rows[y + dy][x + dx] == '#':
                occupied += 1
                break
            elif near or rows[y + dy][x + dx] == 'L':
                break
            unit += 1
            dx = vx * unit
            dy = vy * unit

    return occupied


def get_count(data, near =True):
    tolerance = 4 if near else 5
    rows = data.copy()
    while True:
        total_occupied = 0
        new_rows = []
        for i in range(len(rows)):
            new_row = ''
            for j in range(len(rows[i])):
                seat = rows[i][j]
                if seat == '.':
                    new_row += '.'
                else:
                    occupied = check_occupancy(near, rows, j, i)
                    if seat == 'L' and occupied == 0:
                        new_row += '#'
                        total_occupied += 1
                    elif seat == '#' and occupied >= tolerance:
                        new_row += 'L'
                    else:
                        new_row += seat
            new_rows.append(new_row)
        if new_rows == rows:
            return sum(row.count('#') for row in rows)
        rows = new_rows


print("Part 1: ", get_count(data, True))

print("Part 2: ", get_count(data, False))
