# TODO
def heap(a):
	n=len(a)
	for i in range(n//2,0,-1):
		k=i
		v=a[i]
		heap=False
		while not heap and (2*k)<=n:
			j=2*k
			if j<n:
				if a[j]<a[j+1]:
					a[j]=a[j+1]
					# j+=1
				if v>=a[j]:
					heap=True
				else:
					a[k]=a[j]
					k=j
		a[k]=v

a=[0,2,9,7,6,5,8]
heap(a)
print(a)