class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # same as susbets II -> candidates must be sorted to skip duplicate numnbers!

        def backtrack(i, currSubset, currSum):
            if currSum == target:
                res.append(currSubset.copy()) # must do a copy since it is by reference all ways
                return
            if i >= len(candidates) or currSum > target:
                return

            # decision to add candidates[i]
            


