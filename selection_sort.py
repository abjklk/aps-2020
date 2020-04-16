
def selectionSort(arr):
	for i in range(len(arr)):
	    min_idx = i 
	    for j in range(i+1, len(arr)): 
	        if arr[min_idx] > arr[j]: 
	            min_idx = j         
	    arr[i], arr[min_idx] = arr[min_idx], arr[i] 
	return arr

a=[1,4,3,7,8,4]
print(selectionSort(a))
