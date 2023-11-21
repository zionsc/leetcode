class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = r = 0
        while r < len(nums):
            target -= nums[r]
            while target <= 0:
                min_len = min(min_len, r - l + 1)
                target += nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0 