class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # each node is going to be its parent for now. (start at 0 for the math to make sense, but we won't use it.)
        rank = [1] * (len(edges) + 1)

        def find(node):
            p = parent[n]
            
            while p != parent[p]: # while p is not the ultimate final root node (parent)
                parent[p] = parent[parent[p]] # path compression (to make the path shorter, but does not affect rank[], makes algo more efficient, but not necessary.)
                p = parent[p]
            return p
        

