class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j - 1 >= 0 and j < len(triangle[i - 1]):
                    dp[i][j] = min(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])
                elif j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                elif j < len(triangle[i - 1]):
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
        
        return min(dp[-1])