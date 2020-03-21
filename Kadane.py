# Kadane's Algorithm to print maximum subarray sum along with starting and ending indices
# Time Complexity : O(n)

def kadane(arr,n):
	st=0
	en=0
	c=0
	ma=float("-inf")
	tmax=0
	for i in range(n):
	    tmax+=arr[i]
	    if ma<tmax:
	        ma=tmax
	        st=c
	        en=i
	    if tmax<=0:
	        c=i+1
	        tmax=0
	return [ma,st,en]

arr=[2,-9,4,-1,-2,1,5,-3]
res=kadane(arr,len(arr))
print("Max SubArray Sum is",res[0])
print("Start Index:",res[1])
print("End Index:",res[2])