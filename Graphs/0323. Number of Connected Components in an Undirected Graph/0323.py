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
        
