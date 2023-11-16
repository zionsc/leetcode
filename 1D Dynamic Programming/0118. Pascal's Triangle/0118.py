class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1, 1]]
        if numRows == 1:
            return [dp[0]]
        if numRows == 2:
            return dp
        
        for i in range(1, numRows-1):
            temp = [1]
            for j in range(1, len(dp[i])):
                temp.append(dp[i][j - 1] + dp[i][j])
            temp.append(1)
            dp.append(temp)

        return dp