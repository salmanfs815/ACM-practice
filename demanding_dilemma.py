# T = int(input().strip())
# for i in range(T):
# 	n, m = [int(i) for i in input().strip().split()]
# 	A = [0]*n
# 	for i in range(n):
# 		A[i] = [int(i) for i in input().strip().split()]


T = int(input().strip())
for i in range(T):
	n, m = input().strip().split()
	n = int(n)
	m = int(m)
	A = [[]]*n
	for i in range(n):
		A[i] = tuple(input().strip().split())
	good = True
	for j in range(m):
		count = 0
		for i in range(n):
			if A[i][j] == "1":
				count += 1
		if count != 2:
			good = False
			break
	for i in range(n):
		if A[i] in A[:i] + A[i+1:] and m > 1:
			good = False
	if good:
		print("Yes")
	else:
		print("No")


### attempt 2
# T = int(input().strip())
# for i in range(T):
# 	n, m = [int(i) for i in input().strip().split()]
# 	A = {}
# 	for i in range(n): # i is vertex #
# 		vertices = [int(i) for i in input().strip().split()]
# 		for j in range(len(vertices)): # j is edge #
# 			try:
# 				A[j].append(i)
# 			except:
# 				A[j] = [i]
# 	good = True
# 	for x in A:
# 		num_incidences = len(A[x])
# 		if len(A[x]) != 2:
# 			good = False
# 			break
# 	if good:
# 		print("Yes")
# 	else:
# 		print("No")


### attempt 1
# T = int(input().strip())
# for i in range(T):
# 	n, m = input().strip().split()
# 	n = int(n)
# 	m = int(m)
# 	A = [[]]*n
# 	for i in range(n):
# 		A[i] = tuple(input().strip().split())
# 	good = True
# 	for j in range(m):
# 		count = 0
# 		for i in range(n):
# 			if A[i][j] == "1":
# 				count += 1
# 		if count != 2:
# 			good = False
# 			break
# 	if good:
# 		print("Yes")
# 	else:
# 		print("No")
