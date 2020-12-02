f = open("day2.txt", "r")
raw_list = f.read().split('\n')

def get_range(string):
	return list(map(int,string.split('-')))

def get_dict(string):
	d = {}
	for i in string:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	return d

count = 0
for i in raw_list:
	items = i.split()
	r = get_range(items[0])
	k = items[1][0]
	s = items[2]
	x = get_dict(s).get(k,0)
	if x >= r[0] and x<= r[1]:
		count +=1

print("Part 1: {0}".format(count))

count = 0
for i in raw_list:
	items = i.split()
	r = get_range(items[0])
	k = items[1][0]
	s = items[2]
	index1 = r[0] - 1
	index2 = r[1] - 1
	if (k == s[index1] or k == s[index2]) and (s[index1] != s[index2]):
		count += 1
print("Part 2: {0}".format(count))
	



