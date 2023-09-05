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

        for n1, n2 in edges: # will skip if n1 or n2 are already existing in the map
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
        
        def dfs(i, prev): # currNode, prevNode (keep track of prevNode so we make sure that we can return in non-cyclic case)
            if i in visited: # cycle --> tree cannot have cycle 
                return False
            
            visited.add(i)

            for j in adjacencyList[i]:
                if j == prev: # if found a repeat (continue because it is technically not a cycle, just a return to the prev node)
                    continue
                if not dfs(j, i):
                    return False
            return True


        # dfs must return TRUE meaning there is no cycle, and len(visited) == n meaning that all nodes have been visited. 
        return dfs(0, -1) and len(visited) == n
            
        

            

            
