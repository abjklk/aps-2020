# Program for Pascal's Triangle
# Complexity : O(n^2) time and O(1) extra space

def pascal(n): 

	for line in range(1, n + 1): 
		C = 1 
		for i in range(1, line + 1): 
			print(C, end = " ") 
			C = int(C * (line - i) / i) 
		print()
 
n = 10
pascal(n)