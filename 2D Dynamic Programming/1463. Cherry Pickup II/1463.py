class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        @lru_cache(None)
        def dfs(row, col1, col2):
            if col1 < 0 or col1 >= m or col2 < 0 or col2 >= m:
                return float('-inf')
            res = 0
            res += grid[row][col1]
            if col1 != col2:
                res += grid[row][col2]

            if row != n - 1:
                res += max(dfs(row + 1, new_col1, new_col2)
                        for new_col1 in [col1 - 1, col1, col1 + 1]
                        for new_col2 in [col2 - 1, col2, col2 + 1])
                
            return res
    
        return dfs(0, 0, m - 1)
            