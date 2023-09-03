class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != parent[res]:
                res = parent[parent[res]] # path compression (just simple optimization)
                res = parent[res]

            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            # simple union find --> we can't make it a linked-list right?? --> remember CSCI270 with prof. Cote!
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res



            