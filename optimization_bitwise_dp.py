# Cost Optimization Problem
# Given n jobs along with n workers' cost to do the job, find the minimal cost 
n=3
cost=[[3,2,7],[5,1,3],[2,7,2]]
dp=[float("inf")]*(2**n)
dp[0]=0

def check_set(n):
	ct=0
	while(n):
		n=n&(n-1)
		ct+=1
	return ct

for i in range(2**n):
	x=check_set(i)
	for j in range(n):
		if i|(1<<j)!=i:
			dp[i|(1<<j)]=min(dp[i|(1<<j)],(dp[i]+cost[x][j]))
print(dp)