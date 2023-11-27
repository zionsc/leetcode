class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0

        MOD = 10**9 + 7

        jump = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        dp = [[0] * 10 for _ in range(n + 1)] # dp[i][j] --> i = n, j = 10
        for j in range(10): # make all dp[0][i] = 1 --> 0 digits = 1
            dp[1][j] = 1
        
        for i in range(1, n + 1):
            for j in range(10):
                for k in jump[j]:
                    dp[i][j] += dp[i - 1][k] 
                    dp[i][j] %= MOD
        
        return (sum(dp[n][j] for j in range(10)) % MOD)
