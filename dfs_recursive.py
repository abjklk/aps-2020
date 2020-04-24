# Depth First Traversal of Graph (Recursive)

from collections import defaultdict 

class Graph: 

	# Constructor 
	def __init__(self): 

		self.graph = defaultdict(list) 

	def addEdge(self, u, v): 
		self.graph[u].append(v) 
 

	def DFS(self, v):
		visited[v] = True
		print(v, end = ' ') 

		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFS(i) 
 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
root = 2
print("DFS from root") 
visited = [False] * len(g.graph)
visited[root] = True
g.DFS(root) 
