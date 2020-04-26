# Handout 6
# Program to determine whether the sum of any subset is equal to the given n

def find(arr,l,s):
	for i in range(1,pow(2,l)):
		sm=0
		for j in range(0,l):
			if (i>>j)&1:
				sm+=arr[j]
		if sm==s:
			print("YES")
			return
	
	print("NO")
	return


n = 128
arr = [-1,2,4,121]
find(arr,len(arr),n)

n = 6
arr = [-1,2,4,121]
find(arr,len(arr),n)