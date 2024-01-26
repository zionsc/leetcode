class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, j, remain):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            elif remain == 0:
                return 0

            output = dfs(i + 1, j, remain - 1)
            output += dfs(i - 1, j, remain - 1)
            output += dfs(i, j + 1, remain - 1)
            output += dfs(i, j - 1, remain - 1)

            return output
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7) 