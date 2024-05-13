class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        res=0

        for i in range(n):
            if grid[i][0]==0:
                for j in range(m):
                    grid[i][j]=1 if grid[i][j]==0 else 0
        
        for j in range(m):
            count=0
            for i in range(n):
                count+=1 if grid[i][j]==1 else -1
            if count<0:
                for i in range(n):
                    grid[i][j]=1 if grid[i][j]==0 else 0


        for i in range(n):
            numstr=""
            for j in range(m):
                numstr+=str(grid[i][j])
            res+=int(numstr,2)
        
        return res


