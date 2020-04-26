# Program to check if a given number is perfect or not 
 
def isPerfect( n ): 
	sum = 1
	i = 2
	while i * i <= n: 
		if n % i == 0: 
			sum = sum + i + n/i 
		i += 1
	
	return (True if sum == n and n!=1 else False) 

print(isPerfect(6))
print(isPerfect(420))