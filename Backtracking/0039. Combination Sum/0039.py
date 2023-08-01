class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # i to keep track of what index of candidates[i] we are at 
        def dfs(i, currSubset, currSum):
            # base cases of true or backtrack!
            if currSum == target:
                res.append(currSubset)
                return
            if  i >= len(candidates) or currSum > target:
                return 
            
            # we do include our current ith index!
            currSubset.append(candidates[i])
            dfs(i, currSubset, currSum + candidates[i])
            currSubset.pop() # to remove whatever we just added -> to clean up the recursive tree that we went down

            # we do not include our current ith index!
            dfs(i, currSubset, currSum)

        dfs(0, [], 0)
        return res