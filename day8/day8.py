import copy
r = open("day8.txt", "r")
instructions = []
for i in r.readlines():
	instructions.append([i[:3], int(i[4:].replace('\n', ''))])

def get_acc(instructions):
	acc = 0
	infy = False
	index = 0
	step = [None] * len(instructions) * 1000
	while index < len(instructions):
		operation = instructions[index][0]
		argument = instructions[index][1]
		if operation == 'nop':
			step[index] = True
			index += 1
		elif operation == 'acc':
			step[index] = True
			acc += argument
			index += 1
		elif operation == 'jmp':
			step[index] = True
			index += argument
		if step[index]:
			infy = True
			break
	return acc, infy

part1 = get_acc(instructions)[0]
print("Part 1: {0}".format(part1))

new_acc = 0
for i in range(len(instructions)):
	if instructions[i][0] == 'nop':
		copy_i = copy.deepcopy(instructions)
		copy_i[i][0] = 'jmp'
	elif instructions[i][0] == 'jmp':
		copy_i = copy.deepcopy(instructions)
		copy_i[i][0] = 'nop'

	new_acc, infy = get_acc(copy_i)
	if not infy:
		break
print("Part 2: {0}".format(new_acc))


	


