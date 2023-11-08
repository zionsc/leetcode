class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(fx-sx), abs(fy-sy))
        if dist == 0:
            return t != 1
        return True if dist <= t else False
    
    # difference between euclidean distance, 
    # manhattan distance (costs one to go l r u d, but 2 to go diagonal),
    # chebsyhev distance (costs one to go in all direction)