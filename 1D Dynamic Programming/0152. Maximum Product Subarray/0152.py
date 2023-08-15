class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(res) # [-1] -> then res would be -1. we can't set it to a default val like 1 or 0.
