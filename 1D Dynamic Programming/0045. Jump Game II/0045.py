class Solution:
    def jump(self, nums: List[int]) -> int:
        next_max = 0
        curr_max = 0
        count = 0
        for i in range(len(nums)):
            if curr_max < i:
                count += 1
                curr_max = next_max
            next_max = max(next_max, i + nums[i])
        return count

        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return 0
        
        # dp = [float('inf')] * len(nums) 
        # dp[0] = 0

        # for i in range(len(nums)):
        #     for j in range(nums[i] + 1):
        #         if i + j >= len(nums) - 1:
        #             return dp[i] + 1
        #         dp[i + j] = min(dp[i + j], 1 + dp[i])
            
        # return dp[-1] 
