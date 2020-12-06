# r = open("day6.txt", "r")
# input_data = ""
# for i in r.readlines():
# 	if not i.strip():
# 		input_data += ","
# 	else:
# 		input_data += i.replace('\n', '')

# count = 0
# for item in input_data.split(","):
# 	count += len(set(item))

# print("Part 1: {0}".format(count))


r = open("day6.txt", "r")
fullstring = ""
for i in r.readlines():
	if not i.strip(): # reading blankline
		fullstring += ","
	else:
		fullstring += i.replace('\n', ' ')

input_data = fullstring.split(',')
for i,data in enumerate(input_data):
	data = data.strip()
	if len(data.split(' ')) > 1:
		input_data[i] = data.split(' ')
	else:
		input_data[i] = data

count = 0
for i in input_data:
	if type(i) == str:
		count += len(set(i))
	else:
		count += len(set("".join(i)))
print("Part 2: {0}".format(count))

def get_common_len(arr):
	i = 1
	set1 = set(arr[0])
	while i < len(arr):
		set2 = set(arr[i])
		set1 = set1.intersection(set2)
		i += 1
	return len(set1)

common = 0
for i in input_data:
	if type(i) == str:
		common += len(set(i))
	else:
		common += get_common_len(i)

print("Part 2: {0}".format(common))







