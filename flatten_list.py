# Program to flatten a list of n-dimension to 1-dimension.

def spread(arr):
	res = []
	for i in arr:
		if isinstance(i,list):
			res.extend(i)
		else:
			res.append(i)
	return res

a = [1,2,3,[4,5,6],[7],8,9]
print(spread(a))