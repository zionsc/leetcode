class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i,v in enumerate(nums):
            res ^= n ^ i
        return res