class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows = len(board)
        cols = len(board[0])

        def backtrack(i, r, c):
            if i == len(word):
                return True
            # basically if out of bounds OR 
            if (word[i] != board[r][c] or r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (backtrack(i + 1, r + 1, c) or backtrack(i + 1, r - 1, c) or backtrack(i + 1, r, c + 1) or
                   backtrack(i + 1, r, c - 1))
            path.remove((r, c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c):
                    return True
        
        return False

