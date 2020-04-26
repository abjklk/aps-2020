# Given n determine if n is power of 2.

def isnpow2(n):
	return not n&(n-1)

print(isnpow2(100))
print(isnpow2(16))

# OR
n = 16
print(bin(n).count('1')==1 and n&1==0)