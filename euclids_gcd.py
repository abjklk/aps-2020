# Euclid's GCD algorithm to find HCF of 2 no.s a & b
# Time Complexity O(logn) n is min(a,b)

a = 84
b = 72

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

print(gcd(a,b))