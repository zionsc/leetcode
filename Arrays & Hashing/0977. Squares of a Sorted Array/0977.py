class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,v in enumerate(nums):
            nums[i] *= nums[i]
        return sorted(nums)