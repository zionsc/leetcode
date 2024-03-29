# classic DP approach with aray
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
    
        dp = [0] * n
        dp[n-1] = 1 # can take 1 step to get to n
        dp[n-2] = 2 # can take 1 step to get to n-1, or 2 step to get to n


        for i in range(n-3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]
    
# optimized DP approach with sliding window
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        one, two = 1, 1

        for i in range(n-3, -1, -1):
            temp = one
            one = one + two
            two = one
        
        return one
            