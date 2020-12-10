r = open("day9.txt", "r")
data = list(map(int,r.read().split('\n')))
start = 0
end = 25

def check_valid(num, arr):
 	for i in arr:
 		if (num - i) in arr:
 			return True
 	return False

invalid = -1
while start < len(data) - 5:
	next = data[end]
	if check_valid(next, data[start:end]) == False:
		invalid = next
		break
	start += 1
	end += 1
print("Part 1: {0}".format(invalid))

index = 0
start = 0
total = 0
while start < len(data):
	total += data[index]
	index += 1
	if total > invalid:
		start += 1
		index = start
		total = 0
	elif total == invalid:
		break

contuguous = data[start:index]

low = min(contuguous)
high = max(contuguous)
s = low + high
print("Part 2: {0}".format(s))





