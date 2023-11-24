class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        visited = set()
        res = []

        i, j = 0, 0

        res.append(matrix[i][j])
        visited.add((i, j))

        while len(visited) < m * n:
            # right
            while (i, j + 1) not in visited and j + 1 < m:
                j += 1
                res.append(matrix[i][j])
                visited.add((i, j))

            # down
            while (i + 1, j) not in visited and i + 1 < n:
                i += 1
                res.append(matrix[i][j])
                visited.add((i, j))

            # left
            while (i, j - 1) not in visited and j - 1 >= 0:
                j -= 1
                res.append(matrix[i][j])
                visited.add((i, j))

            # up
            while (i - 1, j) not in visited and i - 1 >= 0:
                i -= 1
                res.append(matrix[i][j])
                visited.add((i, j))

        return res
      