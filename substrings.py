# Handout 2
# Prints all substrings of a string
# Note: Substrings are contiguous

def substring(s,n):
	for i in range(1,n+1):
		for j in range(n-i+1):
			k=j+i-1
			print(s[j:k+1])

substring("hello",len("hello"))