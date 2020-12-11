import copy
r = open("day11.txt", "r")
oridinal_list = r.read().split('\n')
data = []
for i in oridinal_list:
	data.append([j for j in i])

import numpy as np

def rule_one(arr):
	n = len(arr)
	result = copy.deepcopy(arr)
	for i in range(n):
		for j in range(n):
			if i > 0 and i < n-1 and j > 0 and j < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i-1, i+2)]
				if check_adjusent(subset, (1,1)):
					result[i][j] = '#'
			elif i == 0 and j > 0 and j < n-1:
				subset = [arr[x][j-1:j+2] for x in range(i,i+2)]
				print(subset)
				if check_adjusent(subset, (0,1)) and arr[i][j] != '.':
					result[i][j] = '#'
			elif i == n-1 and j > 0 and j < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i-1,i+1)]
				if check_adjusent(subset, (1,1)):
					result[i][j] = '#'
			elif j == 0 and i > 0 and i < n-1 and arr[i][j] != '.':
				subset = [arr[x][j:j+2] for x in range(i-1,i+2)]
				if check_adjusent(subset, (1,0)):
					result[i][j] = '#'
			elif j == n-1 and i > 0 and i < n-1 and arr[i][j] != '.':
				subset = [arr[x][j-1:j+2] for x in range(i-1,i+2)]
				if check_adjusent(subset, (1,1)):
					result[i][j] = '#'
			elif i == 0 and j == 0 and arr[i][j] != '#':
				subset = [arr[x][0:2] for x in range(0,2)]
				if check_adjusent(subset, (0,0)):
					result[i][j] = '#'
			elif i == n-1 and j == 0 and arr[i][j] != '#':
				subset = [arr[x][0:2] for x in range(i-1,i+1)]
				if check_adjusent(subset, (1,0)):
					result[i][j] = '#'
			elif i == 0 and j == n-1 and arr[i][j] != '#':
				subset = [arr[x][j-1:j+1] for x in range(0,2)]
				if check_adjusent(subset, (0,1)):
					result[i][j] = '#'
			elif i == n-1 and j == n-1 and arr[i][j] != '#':
				subset = [arr[x][j-1:j+1] for x in range(i-1,i+1)]
				if check_adjusent(subset, (1,1)):
					result[i][j] = '#'
	return result

def check_adjusent(arr, pos):
	arr[pos[0]][pos[1]] = 'x'
	temp = []
	for i in arr:
		temp += temp + i
	if '#' in temp:
		return False
	return True
print(np.array(rule_one(data)))