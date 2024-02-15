class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        remove_start,remove_end = toBeRemoved

        for start,end in intervals:
            # no overlap
            if end < remove_start or start > remove_end:
                res.append([start, end])
            else:
                # left overlap
                if start < remove_start:
                    res.append([start, remove_start])
                if end > remove_end:
                    res.append([remove_end, end])
        return res