class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # each node is going to be its parent for now. (start at 0 for the math to make sense, but we won't use it.)
        rank = [1] * (len(edges) + 1)