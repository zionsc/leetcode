class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD = 10**9 + 7

        dp = [0 for _ in range(maxLength + 1)]
        dp[0] = 1

        for i in range(maxLength + 1):
            if i - oneGroup >= 0 and i - zeroGroup >= 0:
                dp[i] = dp[i - oneGroup] + dp[i - zeroGroup]
            elif i - oneGroup >= 0:
                dp[i] = dp[i - oneGroup]
            elif i - zeroGroup >= 0:
                dp[i] = dp[i - zeroGroup]
            dp[i] %= MOD
        return sum(dp[minLength:maxLength + 1]) % MOD