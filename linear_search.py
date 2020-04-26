# Program to linearly search x in arr. 
# If x is present then return its index, otherwise return -1 

def search(arr, x): 
	n = len(arr)
	for i in range (n): 
		if arr[i] == x: 
			return i 
	return -1
 
arr = [ 2, 3, 4, 10, 40 ]; 
x = 10; 
n = len(arr); 
print(search(arr, x))