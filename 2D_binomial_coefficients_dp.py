# Algorithm to compute binomial coefficients using DP
# nCk

n = 5
k = 2
li=[[0]*(k+1) for i in range(n+1)]
for i in range(n+1):
	for j in range(min(i,k)+1):
		if j==0 or i==j:
			li[i][j]=1
		else:
			li[i][j]=li[i-1][j-1]+li[i-1][j]
print(li[n][k])