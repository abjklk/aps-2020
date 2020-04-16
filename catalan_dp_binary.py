# How many structurally different binary trees are possible with n nodes?
# DP approach
# Eg, n=3 nodes, result = 5
# n > 1
def catalan_binary_tees(n):
	c=[1 for i in range(n+1)]
	c[2]=2
	for i in range(3,n+1):
		c[i] = 0
		for j in range(i):
			c[i]+=c[j]*c[(i-1)-j]
	return c[n]

print(catalan_binary_tees(5))