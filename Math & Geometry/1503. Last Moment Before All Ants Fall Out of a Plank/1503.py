 class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # The farthest left ant will take its position time to fall off.
        last_left = max(left) if left else 0
        
        # The farthest right ant will take (n - position) time to fall off.
        last_right = n - min(right) if right else 0
        
        # The last moment is the maximum time any ant takes to fall off.
        return max(last_left, last_right)