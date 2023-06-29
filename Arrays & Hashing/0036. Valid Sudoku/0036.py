class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) #
        cols = defaultdict(set) # --> need to store values from each set --> thus must have set in order to check each row/col
        squares = defaultdict(set) # --> key = r//3, c//3 becuase it will then always be 0 1 2 x 0 1 2, checking each of the 9 boards.

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                elif board[r][c] != ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3, c//3]: 
                        return False

                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r//3, c//3].add(board[r][c]) # must do // for integer div --> / returns float point number
        
        return True