class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # i to keep track of what index of candidates[i] we are at 
        def dfs(i, currSubset, currSum):
