class Solution:
    def numSpecial(self, matrix: List[List[int]]) -> int:
        res = 0
        one_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    one_list.append((i, j))
        
        for i, j in one_list:
            row = col = True
            for r in range(len(matrix[i])):
                if matrix[i][r] == 1 and (i,j) != (i,r):
                    row = False
                    break
            for c in range(len(matrix)):
                if matrix[c][j] == 1 and (i,j) != (c,j):
                    col = False
                    break
            if row and col:
                res += 1
        return res

                
        