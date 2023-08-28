class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # each node is going to be its parent for now. (start at 0 for the math to make sense, but we won't use it.)
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            
            while p != parent[p]: # while p is not the ultimate final root node (parent)
                parent[p] = parent[parent[p]] # path compression (to make the path shorter, but does not affect rank[], makes algo more efficient, but not necessary.)
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False # FOUND THE REDUNDANT CONNECTION -> CYCLE DETECTED!
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2] # num of nodes in tree

            else:
                parent[p1]= p2
                rank[p2] += rank[p1]
            
            return True
    
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
        

