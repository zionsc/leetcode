class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=grid[0].copy()

        for i in range(1,n):
            temp=dp.copy()
            for j in range(m):
                best=float('inf')
                for k in range(0,j):
                    best=min(best,dp[k])
                for k in range(j+1,m):
                    best=min(best,dp[k])
                temp[j]=best+grid[i][j]
            dp=temp
        return min(dp)
