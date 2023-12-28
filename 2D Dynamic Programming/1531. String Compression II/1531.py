class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        
        def dfs(i, prev, prev_count, k):
            if (i, prev, prev_count, k) in memo:
                return memo[(i, prev, prev_count, k)]
            if i == len(s):
                return 0
            if k < 0:
                return float('inf')

            if s[i] == prev:
                inc = 1 if prev_count in [1, 9, 99] else 0
                res = inc + dfs(i + 1, prev, prev_count + 1, k)
            else:
                # essentially if they are not the same, I want to remove or keep
                res = min(
                    dfs(i + 1, prev, prev_count, k - 1),
                    1 + dfs(i + 1, s[i], 1, k)
                )
            memo[(i, prev, prev_count, k)] = res
            return res

        return dfs(0, "", 1, k)