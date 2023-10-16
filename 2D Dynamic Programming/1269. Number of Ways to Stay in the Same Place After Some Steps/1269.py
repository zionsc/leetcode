class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = (10 ** 9) + 7
        maxLen = min(arrLen, (steps // 2) + 1)