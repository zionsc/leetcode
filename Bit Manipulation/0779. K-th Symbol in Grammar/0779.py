class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        # basically gets the parent of the number we are looking for as --> two numbers come from each parent.
        # The k-th position in the n-th row is derived from the (k+1)//2-th position in the (n-1)-th row. 
        # 1st and 2nd positions in the n-th row come from the 1st position in the (n-1)-th row.
        # 3rd and 4th positions in the n-th row come from the 2nd position in the (n-1)-th row.
        parent = self.kthGrammar(n - 1, (k + 1) // 2)