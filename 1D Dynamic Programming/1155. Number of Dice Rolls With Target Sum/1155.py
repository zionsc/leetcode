class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        dp[0][0] = 1

        if target < n or target > n * k:
            return 0
        
        for i in range(n + 1):
            for j in range(target + 1):
                for x in range(k + 1):
                    if j - x >= 0:
                        dp[i][j] += dp[i - 1][j - x] % MOD

        return dp[n][target] % MOD