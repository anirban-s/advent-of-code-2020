r = open("day12.txt","r")
original_list = r.read().split('\n')
instructions = [(i[0], int(i[1:])) for i in original_list]

x,y = 0,0
current_direction = 'E'

def move_forward(x,y,current_direction, moves):
	if current_direction == 'E':
		x = x + moves
	elif current_direction == 'W':
		x = x - moves
	elif current_direction == 'N':
		y = y+ moves
	elif current_direction == 'S':
		y = y - moves
	return x,y

def change_direction(current_direction, turn, degree):
	if turn == 'R' and degree == 90:
		if current_direction == 'E':
			return 'S'
		elif current_direction == 'S':
			return 'W'
		elif current_direction == 'W':
			return 'N'
		elif current_direction == 'N':
			return 'E'
	elif turn == 'R' and degree == 180:
		if current_direction == 'E':
			return 'W'
		elif current_direction == 'S':
			return 'N'
		elif current_direction == 'W':
			return 'E'
		elif current_direction == 'N':
			return 'S'
	elif turn == 'R' and degree == 270:
		if current_direction == 'E':
			return 'N'
		elif current_direction == 'S':
			return 'E'
		elif current_direction == 'W':
			return 'S'
		elif current_direction == 'N':
			return 'W'
	elif turn == 'L' and degree == 90:
		if current_direction == 'E':
			return 'N'
		elif current_direction == 'S':
			return 'E'
		elif current_direction == 'W':
			return 'S'
		elif current_direction == 'N':
			return 'W'
	elif turn == 'L' and degree == 180:
		if current_direction == 'E':
			return 'W'
		elif current_direction == 'S':
			return 'N'
		elif current_direction == 'W':
			return 'E'
		elif current_direction == 'N':
			return 'S'
	elif turn == 'L' and degree == 270:
		if current_direction == 'E':
			return 'S'
		elif current_direction == 'S':
			return 'W'
		elif current_direction == 'W':
			return 'N'
		elif current_direction == 'N':
			return 'E'


for inst in instructions:
	action = inst[0]
	moves = inst[1]

	if action == 'F':
		x,y = move_forward(x,y,current_direction, moves)
	elif action == 'E' or action == "W" or action == "N" or action == "S":
		x,y = move_forward(x,y,action, moves)
	elif action == 'L' or action == 'R':
		current_direction = change_direction(current_direction, action, moves)

print("Part 1: {0}".format(abs(x)+abs(y)))


x, y = 0, 0
way_x, way_y = 10, 1
current_direction = 'E'
def move_in_current_direction(x,y,moves,way_x, way_y):
	x = x + way_x * moves
	y = y + way_y * moves
	return x,y
def move_waypoint(way_x,way_y,action, moves):
	if action == 'N':
		way_y = way_y + moves
	elif action == 'S':
		way_y = way_y - moves
	elif action == 'E':
		way_x = way_x + moves
	elif action == 'W':
		way_x = way_x - moves
	return way_x, way_y

def make_turn(action, way_x, way_y):
	if action == 'R':
		return way_y, -way_x
	else:
		return -way_y, way_x

def change_waypoint_direction(action, degree, way_x, way_y):
	no_turns = degree // 90
	for turn in range(1, no_turns+1):
		way_x, way_y = make_turn(action, way_x, way_y)
	return way_x, way_y

for inst in instructions:
	action = inst[0]
	moves = inst[1]

	if action == 'F':
		x,y = move_in_current_direction(x,y, moves, way_x, way_y)
	elif action == 'E' or action == "W" or action == "N" or action == "S":
		way_x,way_y = move_waypoint(way_x,way_y,action, moves)
	elif action == 'L' or action == 'R':
		way_x,way_y = change_waypoint_direction(action, moves, way_x, way_y)

print("Part 2: {0}".format(abs(x)+abs(y)))


