class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[] for i in range(n)]

        for edge in edges:
            self.adj[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append((edge[1], edge[2]))
    
    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstras(node1, node2)
    
    def dijkstras(self, start: int, end: int) -> int:
        minHeap = [(0, start)] # priority queue for dijkstras
        distances = [float('inf')] * len(self.adj)
        distances[start] = 0

        while minHeap:
            curr_distance, curr_node = heapq.heappop(minHeap)

            if curr_distance > distances[curr_node]:
                continue
            
            if curr_node == end:
                return curr_distance
            
            for edge in self.adj[curr_node]:
                nei_node, nei_distance = edge
                new_distance = distances[curr_node] + nei_distance
                if new_distance < distances[nei_node]:
                    distances[nei_node] = new_distance
                    heapq.heappush(minHeap, (new_distance, nei_node))

        return distances[end] if distances[end] != float('inf') else -1
