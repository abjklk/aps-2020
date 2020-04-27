# Longest Increasing Subsequence (DP)
# Time Complexity : O(n^2)
a = [5,11,3,15,30,25]
lis = [1]*len(a)

for i in range(1,len(a)):
	for j in range(i):
		if (a[i]>a[j]) and (lis[j]+1 > lis[i]):
			lis[i] = lis[j]+1

print(lis)