class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if not nums:
        #     return True
        # if len(nums) >= 2 and nums[0] == 0:
        #     return False
        # if len(nums) == 1:
        #     return True
        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i - 1], i + nums[i])
        #     if dp[i] >= len(nums) - 1:
        #         return True
        #     if dp[i] == i:
        #         return False

        max_jump = nums[0]
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            max_jump = max(max_jump, nums[i] + i)
            if max_jump == i and nums[i] == 0:
                return False
            if max_jump >= len(nums) - 1:
                return True