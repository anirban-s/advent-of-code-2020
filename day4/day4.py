import re

r = open("day4.txt", "r")
fullstring = ""
for i in r.readlines():
	if not i.strip():
		fullstring += ","
	else:
		fullstring += i.replace('\n', ' ')

input_list = fullstring.split(',')
for i in range(len(input_list)):
	input_list[i] = input_list[i].strip()

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = "cid"

input_data = []
for i in input_list:
	kv_list = i.split(' ')
	d = {}
	for kv in kv_list:
		key_value = kv.split(':')
		d[key_value[0]] = key_value[1]
	input_data.append(d)


def validate_req(dic):
	keys = list(dic.keys())
	for req in required:
		if req not in keys:
			return False
	return True

valid_count = 0
for d in input_data:
	if validate_req(d):
		valid_count += 1

print("Part 1: {0}".format(valid_count))

def validate_ecl(value):
	ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if value in ecl_list:
		return True
	else:
		return False

def validate_pid(value):
	if len(value) == 9 and value.isnumeric():
		return True
	else:
		return False

def validate_eyr(value):
	x = int(value)
	if x >= 2020 and x<=2030:
		return True
	else:
		return False

def validate_byr(value):
	x = int(value)
	if x >= 1920 and x<=2002:
		return True
	else:
		return False

def validate_iyr(value):
	x = int(value)
	if x >= 2010 and x<=2020:
		return True
	else:
		return False

def validate_hcl(value):
	regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
	p = re.compile(regex)
	if(re.search(p, value)):
		return True
	else:
		return False

def validate_hgt(value):
	unit = value[-2:]
	if unit == 'cm' or unit=='in':
		val = int(value[:-2])
	if unit == 'cm' and val>=150 and val<=193:
		return True
	elif unit == 'in' and val>=59 and val<=76:
		return True
	else:
		return False

valid = 0
for i in input_data:
	if validate_req(i) and validate_ecl(i['ecl']) and validate_pid(i['pid']) and validate_eyr(i['eyr']) and validate_iyr(i['iyr']) and validate_byr(i['byr']) and validate_hcl(i['hcl']) and validate_hgt(i['hgt']):
		valid += 1

print("Part 2: {0}".format(valid))