class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*(n+1) for i in range(m+1)] # must use list comprehension, or everything is by reference
        arr[m-1][n-1] = 1

        print(arr)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                arr[i][j] = arr[i][j+1] + arr[i+1][j]
                arr[m-1][n-1] = 1 # since it updates arr[m-1][n-1] to 0 in the first iteration, but we need it to be 1 HARD CODE LOL        
        
        return arr[0][0]