# Program to evaluate area of a polygon using shoelace formula 

def shoelace(X, Y, n): 

	area = 0
	j = n - 1
	for i in range(n): 
		area += (X[j] + X[i]) * (Y[j] - Y[i]) 
		j = i
	
	return abs(area / 2.0) 

X = [5, 7, 4, 4, 2] 
Y = [5, 3, 1, 3, 4] 
n = len(X) 
print(shoelace(X, Y, n),"sq. units") 