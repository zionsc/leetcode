class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # res = []
        # for c in range(n):
        #     temp = []
        #     for r in range(n - 1, -1, -1):
        #         temp.append(matrix[r][c])
        #     res.append(temp)
        # matrix.clear()
        # matrix.extend(res)
        
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()

