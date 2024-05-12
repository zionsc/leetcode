class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        maxLocal=[[0]*(n-2) for _ in range(n-2)]

        for i in range(len(maxLocal)):
            for j in range(len(maxLocal[i])):
                val=-1
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        val=max(val,grid[k][l])
                maxLocal[i][j]=val
        return maxLocal
