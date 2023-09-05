class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # In the case that there are no nodes, then it is true!
        if not n:
            return True
        
        # to check for loops
        visited = set()
        adjacencyList = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
        
        def dfs(node, prev):
            if node in visited: # cycle
                return False
            
        

            

            
