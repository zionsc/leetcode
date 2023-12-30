class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        
        memo = {}

        # keep track of curr_max in order to add to result if we start a new day
        def dfs(i, d, curr_max):
            if i == len(jobDifficulty):
                return 0 if d == 0 else float('inf')
            if d == 0:
                return float('inf')
            if (i, d, curr_max) in memo:
                return memo[(i, d, curr_max)]
            
            # update curr_max --> since the order of jobDifficulty is not in non-decreasing order necessarily
            curr_max = max(curr_max, jobDifficulty[i])

            # recursive case: 
            # 1. start a new day
            # 2. continue the previous day
            res = min(
                curr_max + dfs(i + 1, d - 1, -1),
                dfs(i + 1, d, curr_max)
            )

            memo[(i, d, curr_max)] = res
            return res

        return dfs(0, d, -1)
