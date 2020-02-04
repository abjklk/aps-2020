# Rod Cutting Problem
# Given a rod of length n, what is the maximum product obtained by cutting the rod into 2 or more pieces?
# DP Approach
n=int(input())

def rod(n):
	result=[0]*(n+1)
	for i in range(2,n+1):
		maxv=0
		for j in range(1,i//2+1):
			maxv=max(maxv,j*(i-j),j*result[i-j])
		result[i]=maxv
	return result[n]


x=rod(n)
print(x)