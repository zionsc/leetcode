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
            
