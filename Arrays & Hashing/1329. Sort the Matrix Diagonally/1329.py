class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        # all row starts --> sort
        # all col starts (from 1st col not 0th) --> sort
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1):
            for j in range(m):
                diag = []
                r,c = i,j
                while r < n and c < m:
                    diag.append(matrix[r][c])
                    r += 1
                    c += 1
                diag.sort()
                print(diag)
                r,c = i,j
                idx = 0
                while r < n and c < m:
                    matrix[r][c] = diag[idx]
                    r += 1
                    c += 1
                    idx += 1
        
        for i in range(1, n):
            diag = []
            for j in range(1):
                r,c = i,j
                while r < n and c < m:
                    diag.append(matrix[r][c])
                    r += 1
                    c += 1
                diag.sort()
                r,c = i,j
                idx = 0
                while r < n and c < m:
                    matrix[r][c] = diag[idx]
                    r += 1
                    c += 1
                    idx += 1
                
                
        return matrix



                
                