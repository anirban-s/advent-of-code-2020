import re
r = open("day7.txt", "r")

rules = {}
pattern = r"(\d+|no)? ?(\w+ \w+) bags?"
for line in r.readlines():
	(_,bag), *inner = re.findall(pattern, line)
	rules[bag] = {inner_bag: int(n) for n, inner_bag in inner if n}

def contain_gold(bag, rules):
	for inner_bag in rules[bag]:
		if contain_gold(inner_bag, rules) or inner_bag == "shiny gold":
			return True
	return False

count = sum([contain_gold(bag, rules)for bag in rules])
print("Part 1: {0}".format(count))


def count_containing_bags(bag, rules):
	return sum([n + n * count_containing_bags(inner_bag, rules) for inner_bag, n in rules[bag].items()])

print("Part 2: {0}".format(count_containing_bags('shiny gold', rules)))