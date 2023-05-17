class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) #adds to set if not found instead of key error
        rows = defaultdict(set) #hashmap for both
        squares = defaultdict(set) #key = (r/3, c/3) 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # if inside already, return false
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                # if it has reached here (if not inside--
                #the hashsets already, then add and iterate again)
                # since the objects are hashsets, key is whatever and the value is a set (multiple values)
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True