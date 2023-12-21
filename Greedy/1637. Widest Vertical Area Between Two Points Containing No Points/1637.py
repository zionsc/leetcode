class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = 0
        points.sort()
        for i in range(1, len(points) - 1):
            res = max(res, points[i][0] - points[i - 1][0]) 
        return res