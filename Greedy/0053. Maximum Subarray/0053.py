class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = float('-inf')
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum