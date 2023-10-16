class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        threes = n // 3
        remainder = n % 3

        if remainder == 0:
            return 3 ** threes
        elif remainder == 1:
            return (3 ** threes-1) * 4
        elif remainder == 2:
            return (3 ** threes) * 2
        
        # pattern is basically multiply as many 3s as you can, but if remainder is 0, then its just the 3s.
        # if remainder is 1, then delete one of the threes, and multiply a 4 (add 1 to one of the threes)
        # if remainder is 2, then basically multiply 2 to the res.