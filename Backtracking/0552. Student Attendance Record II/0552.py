class Solution:
    def checkRecord(self, n: int) -> int:
        MOD=10**9+7
        if (n==0):
            return 1
        if (n==1):
            return 3

        memo=[[[0]*3 for _ in range(2)] for _ in range(n+1)] # memo[idx][numAbsences][consecutiveLate]
        memo[0][0][0]=1

        for idx in range(1,n+1):
            for numAbsence in range(2):
                for consecutiveLate in range(3):
                    # adding P
                    memo[idx][numAbsence][0] += memo[idx-1][numAbsence][consecutiveLate]
                    memo[idx][numAbsence][0] %= MOD

                    # adding A
                    if (numAbsence>0):
                        memo[idx][numAbsence][0] += memo[idx-1][numAbsence-1][consecutiveLate]
                        memo[idx][numAbsence][0] %= MOD

                    # adding L
                    if (consecutiveLate>0):
                        memo[idx][numAbsence][consecutiveLate] += memo[idx-1][numAbsence][consecutiveLate-1]
                        memo[idx][numAbsence][consecutiveLate] %= MOD
        
        res=0
        for numAbsence in range(2):
            for consecutiveLate in range(3):
                res+=memo[n][numAbsence][consecutiveLate]
                res %= MOD
        
        return res