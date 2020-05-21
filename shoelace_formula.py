# Program to evaluate area of a polygon using shoelace formula 

def shoelace(X, Y, n): 
	
	area = 0
	j = n - 1
	for i in range(n): 
		area += (X[j] + X[i]) * (Y[j] - Y[i]) 
		j = i
	
	return abs(area / 2.0) 

X = [180, 323, 390, 347, 216, 170]
Y = [149, 122, 209, 349, 333, 267]
n = len(X) 
print(shoelace(X, Y, n),"sq. units") 