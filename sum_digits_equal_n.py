# Handout 5
# Program to print numbers whose sum of digits is equal to n

def getSum(num,n):
	s = 0
	while(num):
		s+=num%n
		num//=n
	return s

def getN(num,n):
	s = getSum(num,n)
	if s%n == 0:
		return num*n
	extra = n - (s%n)
	return (num*n)+extra

n = 10
for i in range(1,n+1):
	print(getN(i,n))