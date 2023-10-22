class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # intialize to the first and last sectors in rounds array
        a, b = rounds[0], rounds[-1]
        
        # meaning we NEVER CROSSED the start and started again
        if a <= b: 
            return [i for i in range(a, b + 1)]
        # meaning we DID CROSS the start and started again
        else:
            return [i for i in range(1, b + 1)] + [i for i in range(a, n + 1)]