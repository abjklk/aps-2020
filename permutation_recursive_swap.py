# Handout 1
# Program to recursively compute all permutations of a string / list by swapping indices

def compute(a,l,r):
	if l==r:
		print("".join(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			compute(a,l+1,r)
			a[l], a[i] = a[i], a[l]


a = "ABC"
compute(list(a),0,len(a)-1)