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
            currSubset.append(candidates[i])
            backtrack(i + 1, currSubset, currSum + candidates[i])
            currSubset.pop() # to clean up that recursive subtree

            # decision to not add candidate[i], must skip duplicates, this is why we sorted the array first
            while i < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, currSubset, currSum)

        backtrack(0, [], 0)
        return res


