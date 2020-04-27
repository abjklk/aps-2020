# Ways to sum 3,5,10 in order to reach n
# The Coin Change Problem
# Eg. 15 => (3+3+3+3+3),(5+5+5),(10+5).  
# DP approach

def loop(x,n):
	for i in range(x,n+1):
		result[i]+=result[i-x]


n=int(input())

result=[0]*(n+1)
result[0]=1


for i in list(map(int,input().split())):
	loop(i,n)
	# print(result)
print(result[-1])

