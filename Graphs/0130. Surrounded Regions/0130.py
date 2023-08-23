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
            
            visitSet.add((r, c))
            board[r][c] = "T" # make unchanging values into temp variable so we can freely go through entire board to change all O's that will change to X's.

            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

        for c in range(cols):
            bfs(0, c)
            bfs(rows - 1, c)

        for r in range(rows):
            bfs(r, 0)
            bfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        


