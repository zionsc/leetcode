class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        perfect_squares = []

        # noting perfect squares 
        for i in range(n + 1):
            if int(int(sqrt(i)) * int(sqrt(i))) == i:
                perfect_squares.append(i)

        for i in range(1, n + 1):
            for square in perfect_square:
                if i - square >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - square])
                    
        return dp[n]