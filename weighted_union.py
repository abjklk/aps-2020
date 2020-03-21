def root(a,i):
	while(a[i]!=i):
		i=a[i]
	return i
def weighted_union(a,size,u,v):
	rootu=root(a,u)
	rootv=root(a,v)
	if size[rootu]<size[rootv]:
		a[rootu]=a[rootv]
		size[rootv]+=size[rootu]
	else:
		a[rootv]=a[rootu]
		size[rootu]+=size[rootv]

a=[0,1,2,3,4,5]
size=[1]*len(a)
weighted_union(a,size,0,1)
weighted_union(a,size,0,2)
weighted_union(a,size,3,2)
print(a)
print(size)