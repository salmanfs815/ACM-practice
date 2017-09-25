while True:
	n = int(input().strip())
	if n == 0:
		break
	rules = []
	for i in range(n):
		before = input().strip()
		after = input().strip()
		rules.append([before, after])
	string = input().strip()
	for rule in rules:
		strlen = len(rule[0])
		while True:
			idx_start = string.find(rule[0])
			if idx_start == -1:
				break
			string = string[:idx_start] + rule[1] + string[idx_start+strlen:]
	print(string)
