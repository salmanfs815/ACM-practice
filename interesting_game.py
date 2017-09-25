T = int(input())
for i in range(1,T+1):
	N, K, X = input().strip().split()
	N = int(N)
	K = int(K)
	X = int(X)
	weight = ((-1/2)*(1-X)*(1+X-1)) + ((-1/2)*(X+K-N-1)*(X+K+N))
	print("Case {}: {}".format(i, int(weight)))
