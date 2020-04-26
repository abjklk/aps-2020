# Program to determine the number of bits set in a number using bitwise ops.

def countSet(n):
	ct = 0
	while(n):
		n&=(n-1)
		ct+=1
	return ct

n = 81963
print(countSet(n))


# OR
# use bin(n).count('1')