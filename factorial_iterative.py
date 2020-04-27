# Program to find factorial of given number (Iterative)
# Time Complexity : O(n)

def factorial(n):
	product = 1
	for i in range(2,n+1):
		product *= i
	return product

a = 10
print(factorial(a))