# Ways to sum 3,5,10 in order to reach n
# Eg. 15 => (3+3+3+3+3),(5+5+5),(10+5).  
# DP approach

def loop(x,n):
	for i in range(x,n+1):
		result[i]+=result[i-x]



n=int(input())

result=[0]*(n+1)
result[0]=1

def rec(x):
	if x<=3:
		return x
	return rec(x-3)

def pr():
	for i in range(n):
		if result[n-i]>0:
			print(rec(i))

for i in list(map(int,input().split())):
	loop(i,n)
	print(result)
	pr()


"""
complete this
Coin change problem
Salary(codechef)
journey to the moon(hackerank)
"""
