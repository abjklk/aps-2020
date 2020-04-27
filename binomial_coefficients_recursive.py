# Recursive Algorithm to compute binomial coefficients
# nCk

n = 5
k = 2

def bc(n,k):
	if n==k or k==0:
		return 1
	return bc(n-1,k-1)+bc(n-1,k)

print(bc(n,k)) #5C2 = 10