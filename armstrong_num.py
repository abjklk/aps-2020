# Program to determine whether the number is Armstrong number or not 

def armstrong(n):
	c = n
	s = 0
	while(n):
		s+=(n%10)**3
		n//=10
	if s == c:
		return True
	return False 

n = 371
print(armstrong(n))