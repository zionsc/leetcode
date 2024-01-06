class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # we want to take this start time, or take optimal solution before it 
        n = len(startTime)
        dp = [0] * (n + 1) # for the first iteration we need to go out of bounds 

        # keep track of the start time and the index in order to match with the endtime and profit later
        start = [(startTime[i], i) for i in range(n)]


        # we take the job, or we take the optimal solution that was considered before our job (dp[i + 1])
        dp[i] = max(dp[i + 1], profit[start[i][1]] + dp[next_compatible])