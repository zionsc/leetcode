class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0

        for i,a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesome = a + nums[l] + nums[r]
                if threesome >= target:
                    r -= 1
                else:
                    res += r - l
                    l += 1
        return res