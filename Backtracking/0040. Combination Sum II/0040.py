class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # same as susbets II -> candidates must be sorted to skip duplicate numnbers!

