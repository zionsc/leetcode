class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visitSet = set()

        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visitSet or board[r][c] == "X":
                return
            
