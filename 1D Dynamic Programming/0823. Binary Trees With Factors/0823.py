class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        # the reason we sort is because we would break out of the loop earlier since we want to check i for being the parent
        # and j for being a possible child nodde
        arr.sort()
        my_set = set()
        dp = { x : 1 for x in arr }

        for i in range(len(arr)):
            for j in range(len(arr)):
                if j > i**0.5: # if at any point j > sqrt(i) then break, move onto next i (36 --> 6, nothing above 6 can make 36)
                    break

                if i // j in my_set and i % j == 0: # if the value is in the set, and also if j is a factor of i. (basically is it possible to be a child?)
                    if i // j == j: # j * j == i
                        dp[i] += dp[j] * dp[j]
                    else: # j * something == i
                        dp[i] += dp[j] * dp[i // j] * 2 # since there are two arrangements (j * val and val * j)
                    dp[i] %= MOD
        return sum(dp.values()) % MOD





        