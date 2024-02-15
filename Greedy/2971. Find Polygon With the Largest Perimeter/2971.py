class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix_sum = []
        prefix = 0
        for i,v in enumerate(nums):
            prefix += v
            prefix_sum.append(prefix)
        
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < prefix_sum[i - 1]:
                return prefix_sum[i]
        
        return -1
