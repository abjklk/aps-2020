# Handout 4
# Program to obtain substrings of string using bitwise shift op

a = "ABCD"
n = len(a)
for i in range(1<<n):
	for j in range(n):
		if i&(1<<j):
			print(a[j],end="")
	print()