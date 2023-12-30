class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n - 1, 0, -1):
            for j in range(n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = 0 if j - i < 2 else dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[1][n] <= k