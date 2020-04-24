class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 
          
   
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
  
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
        ct = 0
        for u,v,weight  in result: 
            ct+=weight
        print(ct)
  
a=list(map(int,input().split()))
N=a[0]
M=a[1]
g = Graph(N)
for i in range(M):
    x=list(map(int,input().split()))
    g.addEdge(x[0]-1,x[1]-1,x[2])
  
g.KruskalMST() 


#input
# 7 12
# 1 2 16
# 1 3 12
# 1 4 21
# 2 4 17
# 2 5 20
# 3 4 28
# 3 6 31
# 4 5 18
# 4 6 19
# 4 7 23
# 5 7 11
# 6 7 27