class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
    
        dp = [0] * n
        dp[n-1] = 1 # can take 1 step to get to n
        dp[n-2] = 2 # can take 1 step to get to n-1, or 2 step to get to n
        

