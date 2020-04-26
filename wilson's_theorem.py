# This theorem states that a number n is prime when (n-1)! mod n = n - 1
# Applicable only for small n as (n-1)! is expensive for large n
import math

def isPrime(n):
	return math.factorial(n-1)%n == n-1

print(isPrime(17))