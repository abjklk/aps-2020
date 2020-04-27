# Program to demonstrate bubble sort.

def bubble(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

a=[1,4,3,7,8,4]
print(bubble(a))
