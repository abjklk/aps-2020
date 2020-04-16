# Given n print the nth Catalan Number (1-based indexing)
# Recursive Approach
# Eg. 1,1,2,5,42...
# n = 5 
# ans:42

def catalan(n):
	if n<=1:
		return 1
	res = 0
	for i in range(n):
		res+=catalan(i)*catalan(n-i-1)
	return res

print(catalan(5))
