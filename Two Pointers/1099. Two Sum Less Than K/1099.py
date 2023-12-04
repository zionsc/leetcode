class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1
        l, r = 0, len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]
            if sum < k:
                res = max(res, sum)
                l += 1
            else:
                r -= 1
        return res