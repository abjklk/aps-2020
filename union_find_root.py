# todo
def root(a,i):
	while(a[i]!=i):
		i=a[i]
	return i
def find(a,u,v):
	if root(a,u) == root(a,v):
		return 1
	return 0

def union(a,u,v):
	rootu = root(a,u)
	rootv = root(a,v)
	a[rootu] = rootv

vertex=[0,1,2,3,4,5,6]
edges=[(1,0),(1,3),(4,6),(2,6)]
for edge in edges:
	union(vertex,edge[0],edge[1])
print(vertex)
print(find(vertex,1,5))