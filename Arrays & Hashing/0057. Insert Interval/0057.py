class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:(x[0]))

        res = []
        start,end = intervals[0][0],intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append([start,end])
                start,end = intervals[i][0],intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        
        res.append([start,end])
        return res
        