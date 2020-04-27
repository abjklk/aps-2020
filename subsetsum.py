# Subset Sum using DP
# Given array, is it possible to get a subset sum equal to query?

ss=[1,2,3,5,7]
sum = 9
items=len(ss)
a=[[1]+([0]*sum)]*(items+1)
print(a)
for i in range(1,items+1):
	for j in range(1,sum+1):
		if a[i-1][j]==1:
			a[i][j]=1
		else:
			if ss[i-1]>j:
				continue
			else:
				a[i][j]=a[i-1][j-ss[i-1]]

# print(a)
