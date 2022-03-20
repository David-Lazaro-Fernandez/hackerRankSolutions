from collections import defaultdict
from telnetlib import STATUS

class Graph: 
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DLS(self, src, tgt, depth):
        if(src == target):
            return True
        if(depth < 0): 
            return False 
        for i in self.graph[src]:
            path[maxDepth].append(str(src)+'-'+str(i))
            print   