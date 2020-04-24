# Breadth First Search of Graph using queue 

vertex=[0,1,2,3,4,5,6]
edges=[(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]

adjacencyList=[[] for v in vertex]

for edge in edges:
	adjacencyList[edge[0]].append(edge[1])
# print(adjacencyList)

queue=[vertex[0]] #or start with root
visited=[]

while queue:
	current = queue.pop()
	for neighbor in adjacencyList[current]:
		if not neighbor in visited:
			queue.insert(0,neighbor)
	visited.append(current)
print(visited)
