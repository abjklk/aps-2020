# Program to print primes smaller than n using Sieve of Sundaram. 

def SieveOfSundaram(n): 
	
	nNew = int((n - 2) / 2)
	marked = [0] * (nNew + 1) 

	for i in range(1, nNew + 1): 
		j = i
		while((i + j + 2 * i * j) <= nNew): 
			marked[i + j + 2 * i * j] = 1 
			j += 1
	if (n > 2): 
		print(2, end = " "); 

	for i in range(1, nNew + 1): 
		if (marked[i] == 0): 
			print((2 * i + 1), end = " ")

n = 99 
SieveOfSundaram(n)
