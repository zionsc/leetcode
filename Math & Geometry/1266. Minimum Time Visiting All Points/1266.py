class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            
            # essentially because the maximum of the distances between the x and y coordinates determine the time
            # since we can also go diagonally.
            res += max(abs(target_x - curr_x), abs(target_y - curr_y))

        return res