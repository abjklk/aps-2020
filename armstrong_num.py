# Program to determine whether the number is Armstrong number or not 
# Time Complexity : O(n), n-> no.of digits 
import math

def armstrong(n):
	c = n
	d = math.floor(math.log10(c)+1)
	s = 0
	while(n):
		s+=(n%10)**d
		n//=10
	if s == c:
		return True
	return False 

n = 1634
print(armstrong(n))