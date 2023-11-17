class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]