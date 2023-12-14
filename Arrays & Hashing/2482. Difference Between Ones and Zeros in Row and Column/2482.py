class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row = [0]*m
        col = [0]*n
        
        # just make and return diff
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        
        diff = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = row[i] + col[j] - (n - row[i]) - (m - col[j])
        
        return diff

                
        