class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        discovered = set() # (r, c)
        maxArea = 0
        currArea = 0 # must keep track of currArea in order to not split between recursive trees!

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in discovered or grid[r][c] == 0:
                return
            
            nonlocal maxArea
            nonlocal currArea
            
            currArea += 1
            maxArea = max(maxArea, currArea)
            discovered.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        