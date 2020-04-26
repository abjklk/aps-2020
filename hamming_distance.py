# Program to determine hamming distance 

def hammingDistance(n1, n2) : 

	x = n1 ^ n2 #xor op to  determine bit differences
	setBits = bin(x).count('1') #counting the set bits
	return setBits

n1 = 9
n2 = 14
print(hammingDistance(9, 14)) 
