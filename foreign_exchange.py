
while True:
	n = int(input())
	if n == 0:
		break
	data = {}
	for i in range(n):
		original, target = input().strip().split()
		original = int(original)
		target = int(target)
		data[original] = target
	changed = True
	while len(data) > 0 and changed:
		a, b = data.popitem()
		if data[b] = a