class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = (10 ** 9) + 7
        maxLen = min(arrLen, (steps // 2) + 1)

        dp = [[0] * maxLen for i in range(steps + 1)]
        dp[0][0] = 1 # [steps][index]

        for step in range(1, steps + 1):
            for index in range(maxLen):

                # stayed previously
                dp[step][index] += dp[step - 1][index]

                # moved left previously
                if index > 0:
                    dp[step][index] += dp[step - 1][index + 1]

                # moved right previously 
                if index < maxLen - 1:
                    dp[step][index] += dp[step - 1][index - 1]

                # modulo at each step to not overflow
                dp[step][index] %= mod

        return dp[step][0]