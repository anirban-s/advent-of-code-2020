r = open("day5.txt", "r")
input_data = r.read().split('\n')

def get_row(string):
	lower = 0
	upper = 127
	for i in string:
		if i == 'F':
			upper = (upper - lower) // 2 + lower
		if i == 'B':
			lower = (upper + 1 - lower) // 2 + lower
	if lower == upper:
		return lower

def get_col(string):
	lower = 0
	upper = 7
	for i in string:
		if i == 'L':
			upper = (upper - lower) // 2 + lower
		if i == 'R':
			lower = (upper + 1 - lower) // 2 + lower
	if lower == upper:
		return lower

seatids = []
for item in input_data:
	row = item[:-3]
	col = item[-3:]
	seat_id = get_row(row) * 8 + get_col(col)
	seatids.append(seat_id)
maxseatid = max(seatids)
print("Part 1: {0}".format(maxseatid))


minseatid = min(seatids)
for i in range(minseatid, maxseatid+1):
	if i not in seatids:
		print("Part 2: {0}".format(i))
		break

