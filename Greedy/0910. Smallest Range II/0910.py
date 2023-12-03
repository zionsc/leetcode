class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        small = nums[0]
        big = nums[-1]
        score = big - small
        
        for i in range(len(nums) - 1):
            score = min(score, max(big - k, nums[i] + k) - min(small + k, nums[i + 1] - k))
        
        return score