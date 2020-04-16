# Algorithm to compute binomial coefficients using DP with O(1) auxiliary space
# nCk

n = 5
k = 2
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
	for j in range(min(i,k),0,-1):
		dp[j] = dp[j] + dp[j-1]
print(dp[k])