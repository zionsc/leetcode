class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and j > 0:
                    dp[i][j] += dp[i][j - 1] + dp[i - 1][j]
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]
        
        return dp[-1][-1]