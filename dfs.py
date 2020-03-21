vertex=[0,1,2,3,4,5,6]
edges=[(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]

adjacencyList=[[] for v in vertex]

for edge in edges:
	adjacencyList[edge[0]].append(edge[1])
print(adjacencyList)

stack=[vertex[0]] #or start with root
visited=[]
while stack:
	current=stack.pop()
	for neighbor in adjacencyList[current]:
		if not neighbor in visited:
			stack.append(neighbor)
	visited.append(current)
print(visited)
