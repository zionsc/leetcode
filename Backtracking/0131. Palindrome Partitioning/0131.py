class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []

        def dfs(i):
            if i >= len(s):
                res.append(currPartition.copy())
                return