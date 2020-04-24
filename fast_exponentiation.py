# Given two numbers base and exp, we need to compute base^exp.

# Program to compute exponential value using (2^k) -ary method. 

def exponentiation(bas, exp): 
	t = 1
	while(exp > 0): 

		if (exp % 2 != 0): 
			t = (t * bas) 

		bas = (bas * bas) 
		exp = int(exp / 2)
	return t 

bas = 27926 
exp =7819 
print(exponentiation(bas,exp))
