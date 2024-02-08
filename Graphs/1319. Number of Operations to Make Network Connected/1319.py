class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
    
        self.num_networks = 0
        self.adj_list = defaultdict(list)

        for a,b in connections: 
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in self.adj_list[node]:
                dfs(nei)

        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                self.num_networks += 1
        
        return self.num_networks - 1
