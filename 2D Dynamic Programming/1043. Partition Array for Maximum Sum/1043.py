class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n):
            curr_sum = curr_max = 0
            for j in range(i, max(-1, i - k), -1):
                if curr_max < arr[j]:
                    curr_max = arr[j]
                curr = curr_max * (i - j + 1) + dp[j]
                if curr_sum < curr:
                    curr_sum = curr
            dp[i + 1] = curr_sum
        return dp[-1]