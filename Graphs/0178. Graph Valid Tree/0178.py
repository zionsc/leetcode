class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjacencyList = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for j in adjacencyList[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visit)

            

            
