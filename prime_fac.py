# Program to find prime factors of a number
# Time Complexity O(sqrt(n))

import math

def fac(n):
	f = []
	for i in range(2,int(math.sqrt(n))+1):
		while n%i==0:
			f.append(i)
			n//=i
	if n>1:
		f.append(n)
	return f

n = int(input())
print(fac(n))