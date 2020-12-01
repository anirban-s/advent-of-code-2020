f = open("day1.txt", "r")
arr = list(map(int,f.read().split()))
num1, num2 = 0,0
for i in arr:
	if (2020 - i) in arr:
		num1, num2 = i , 2020-i
		break

print("Part 1 : {0}".format(num1*num2))

num3 = 0

for i in range(len(arr)):
	for j in range(len(arr)):
		if arr[i] != arr[j]:
			if (2020 - (arr[i] + arr[j])) in arr:
				num1 = arr[i]
				num2 = arr[j]
				num3 = 2020 - (arr[i] + arr[j])

print("Part 2 : {0}".format(num1*num2*num3))





