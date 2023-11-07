class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [ d / s for d, s in zip(dist, speed) ]