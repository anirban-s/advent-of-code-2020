from collections import defaultdict
r = open("day10.txt", "r")
data = list(map(int, r.read().split('\n')))

data = sorted(data)
ones = 1
threes = 1
for i in range(len(data)-1):
	diff = data[i+1] - data[i]
	if diff == 1:
		ones += 1
	else:
		threes += 1

mul = ones * threes
print("Part 1: {0}".format(mul))


def count_variations(jolts):
    tries = defaultdict(int)
    tries[0] = 1
    for jolt in jolts:
        tries[jolt] = sum([tries[jolt - d] for d in [1, 2, 3]])

    return tries[jolts[-1]]

variations = count_variations(data)
print("Part 2: {0}".format(variations))

			
