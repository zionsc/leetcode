class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        dp = [defaultdict(int) for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]
        return res