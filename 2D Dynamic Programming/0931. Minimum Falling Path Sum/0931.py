class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0].copy()
        
        for i in range(1, n):
            temp = [float('inf')] * n
            for j in range(n):
                temp[j] = min(temp[j], dp[j] + matrix[i][j])
                if j - 1 >= 0:
                    temp[j] = min(temp[j], dp[j - 1] + matrix[i][j])
                if j + 1 < n:
                    temp[j] = min(temp[j], dp[j + 1] + matrix[i][j])
            dp = temp
        return min(dp)
        
