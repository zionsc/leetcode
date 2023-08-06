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
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

            
        backtrack(0)
        return res
