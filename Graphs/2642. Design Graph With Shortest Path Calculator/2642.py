class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[] for i in range(n)]

        for edge in edges:
            self.adj[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append((edge[1], edge[2]))
    
    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstras(node1, node2)
    
    def dijkstras(self, node1: int, node2: int) -> int:
        minHeap = [(node1, 0)] # priority queue for dijkstras
        distances = [float('inf')] * len(self.adj)
        distances[node1] = 0

        while minHeap:
            

