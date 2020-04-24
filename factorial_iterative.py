# Program to find factorial of given number (Iterative)
# Time Complexity : O(n)

def factorial(n):

	return 1 if (n == 1 or n == 0) else n * factorial(n - 1)  
  
a = 10
print(factorial(a))