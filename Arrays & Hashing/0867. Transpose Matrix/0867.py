class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])

        res = [[0 for _ in range(r)] for _ in range(c)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j][i] = matrix[i][j]
        return res