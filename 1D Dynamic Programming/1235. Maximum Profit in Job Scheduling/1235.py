class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # we want to take this start time, or take optimal solution before it 
        n = len(startTime)
        dp = [0] * (n + 1) # for the first iteration we need to go out of bounds 

        # keep track of the start time and the index in order to match with the endtime and profit later
        start = [(startTime[i], i) for i in range(n)]
        start.sort()

        for i in range(n - 1, -1, -1):
            # look for the next optimal one that starts after current one ends (binary search)
            # the 0 next to endTime is just placeholder since we have to search for a tuple in start array
            next_compatible = bisect.bisect_left(start, (endTime[start[i][1]], 0), i + 1)
            # we take the job, or we take the optimal solution that was considered before our job (dp[i + 1])
            dp[i] = max(dp[i + 1], profit[start[i][1]] + dp[next_compatible])
        return dp[0]