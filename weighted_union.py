# Union Find with weighted union function
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

def find(arr,a,b):
	if arr[a]==arr[b]:
		return True
	else:
		return False

vertex=[0,1,2,3,4,5,6]
size=[1]*len(vertex)
edges=[(1,0),(1,3),(4,6),(2,6)]
for edge in edges:
	weighted_union(vertex,size,edge[0],edge[1])
print(vertex)
print(find(vertex,1,5))