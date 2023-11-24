class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        start, end = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] > end:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])

        res.append([start, end])
        return res