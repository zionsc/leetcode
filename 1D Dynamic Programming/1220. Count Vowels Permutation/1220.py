class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 0
        if n == 1:
            return 5

        # Initialize the counts for each vowel
        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(2, n + 1):
            a_new = (e) % MOD
            e_new = (a + i) % MOD
            i_new = (a + e + o + u) % MOD
            o_new = (i + u) % MOD
            u_new = (a) % MOD

            a, e, i, o, u = a_new, e_new, i_new, o_new, u_new

        return (a + e + i + o + u) % MOD