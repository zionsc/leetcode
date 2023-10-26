class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        # the reason we sort is because we would break out of the loop earlier since we want to check i for being the parent
        # and j for being a possible child nodde
        arr.sort()
        s = set()
        dp = { x : 1 for x in arr }
        