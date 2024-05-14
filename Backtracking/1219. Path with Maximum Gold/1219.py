class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res=0
        row,col=len(grid),len(grid[0])

        def dfs(r,c,currSum):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0 or (r,c) in visited:
                return 0
            
            currSum+=grid[r][c]
            self.res=max(self.res,currSum)
            visited.add((r,c))
            dfs(r+1,c,currSum)
            dfs(r-1,c,currSum)
            dfs(r,c+1,currSum)
            dfs(r,c-1,currSum)
            visited.remove((r,c))
        
        for r in range(row):
            for c in range(col):
                visited=set()
                dfs(r,c,0)
        return self.res