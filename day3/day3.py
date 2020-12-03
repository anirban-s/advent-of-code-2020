s = open("day3.txt", "r")

li = s.read().split("\n")
m = len(li)
n = len(li[0])

def count_trees(right, down):
	character_needed = (m-1)*right + 1 # in the last line
	no_of_repeat = (character_needed // n) + 1

	arr = []

	for i in li:
		temp = []
		for j in i:
			temp.append(j)
		arr.append(temp * no_of_repeat)

	i = 0
	j = 0
	count = 0

	while i < m:
		if (arr[i][j]) == '#':
			count += 1
		j += right
		i += down
	return count

print("Part 1: {0}".format(count_trees(3,1)))

routes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

trees_mul = 1
for route in routes:
	trees_mul *= count_trees(route[0],route[1])

print("Part 2: {0}".format(trees_mul))