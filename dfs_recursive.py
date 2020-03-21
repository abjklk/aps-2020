from collections import defaultdict

n=4
vertex=list(range(n))
edges=[(0,1),(0,2),(1,2),(2,0),(2,3),(3,3)]

adjacencyList=defaultdict(list)
for edge in edges:
	adjacencyList[edge[0]].append(edge[1])

def dfs(edges, n, src):
	visited.append(src)
	for i in range(n):
		if(vertex[i] in adjacencyList[src] and vertex[i] not in visited):
			print(i,end=" ")
			dfs(edges, n, i)

src=vertex[2]
visited=[]
print(src,end=' ')
dfs(adjacencyList,n,src)      