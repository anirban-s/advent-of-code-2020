import copy
r = open("test.txt", "r")
oridinal_list = r.read().split('\n')
data = []
for i in oridinal_list:
	data.append([j for j in i])

import numpy as np

def rule_two(arr):
	n = len(arr)
	result = copy.deepcopy(arr)
	for i in range(n):
		for j in range(n):
			if i > 0 and i < n-1 and j > 0 and j < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i-1, i+2)]
				if count_hash(subset, (1,1)) >= 4:
					result[i][j] = 'L'
			elif i == 0 and j > 0 and j < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i,i+2)]
				if count_hash(subset, (0,1)) >= 4:
					result[i][j] = 'L'
			elif i == n-1 and j > 0 and j < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i-1,i+1)]
				if count_hash(subset, (1,1)) >= 4:
					result[i][j] = 'L'
			elif j == 0 and i > 0 and i < n-1 and arr[i][j] != '.':
				subset = [arr[x][j:j+2] for x in range(i-1,i+2)]
				if count_hash(subset, (1,0)) >= 4:
					result[i][j] = 'L'
			elif j == n-1 and i > 0 and i < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i-1,i+2)]
				if count_hash(subset, (1,1)) >= 4:
					result[i][j] = 'L'
	return result

def count_hash(arr, pos):
	count = 0
	arr[pos[0]][pos[1]] = 'x'
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] == '#':
				count += 1
	return count

print(np.array(rule_two(data)))