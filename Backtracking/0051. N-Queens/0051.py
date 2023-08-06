class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # basically iterate through rows, have a set for cols, posDiag, negDiag
        cols = set()
        posDiag = set() # (r + c) topleft -> bottomright
        negDiag = set() # (r - c) bottomleft -> topright

        res = []
        board =[["."] * n for i in range(n)] # n x for i in range(n) (cols)

        def backtrack(r):
            if r == n: # when we iterate through all the rows
                copy = ["".join(row) for row in board]
                res.append(copy)
            for c in range(n):
                if c in cols or (r + c)
