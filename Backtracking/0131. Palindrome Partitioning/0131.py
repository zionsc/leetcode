class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []

        def dfs(i):
            if i >= len(s):
                res.append(currPartition.copy()) # if we got to the end, that means we can just add whatever it added as a palindrome
                return