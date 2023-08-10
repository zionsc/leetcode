class Solution:
    def rob(self, nums: List[int]) -> int:  
        # basically run house robber I twice on the nums[1:] and nums[:-1] (because we can't have the last and first values together selected)

    def helper(self, nums):
        rob1, rob2 = 0, 0
        