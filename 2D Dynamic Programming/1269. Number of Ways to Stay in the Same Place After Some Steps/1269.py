class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = (10 ** 9) + 7
        maxLen = min(arrLen, (steps // 2) + 1)

        dp = [[0] * maxLen for i in range(steps + 1)]
        dp[0][0] = 1