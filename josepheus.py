# Josepheus Problem iterative given n,k

def josepheus(n,k):
	res=0
	for i in range(1,n+1):
		res=(res+k)%i
	return res+1


print(josepheus(14,1))