class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        small = nums[0]
        big = nums[-1]
        score = big - small
        
        for i in range(len(nums) - 1):
            # testing all ranges possibly simply nums[i] + k could be slightly bigger than big-k!
            # nums[i + 1] - k might be smaller smaller than small + k
            score = min(score, max(big - k, nums[i] + k) - min(small + k, nums[i + 1] - k))
        
        return score