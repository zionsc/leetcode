class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # basically iterate through rows, have a set for cols, posDiag, negDiag
        cols = set()
        posDiag = set()
        negDiag = set()

        res = []
        board =[["."] * n for i in range(n)] # n x for i in range(n) (cols)