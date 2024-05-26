#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int checkRecord(int n) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<vector<vector<int>>>memo(vector<int>(vector<int>(0, 3), 2), n+1);
        memo[0][0][0]=1;

        int MOD=10**9+7;
        int res=0;

        for (int idx=1; idx<n+1; idx++) {
            for (int numAbsence=0; numAbsence<2; numAbsence++) {
                for (int consecutiveLate=0; consecutiveLate<3; consecutiveLate++) {
                    // adding P
                    memo[idx][numAbsence][0]+=memo[idx-1][numAbsence][consecutiveLate];
                    memo[idx][numAbsence][0]%=MOD;

                    // adding A
                    if (numAbsence>0) {
                        memo[idx][numAbsence][0]+=memo[idx-1][numAbsence-1][consecutiveLate];
                        memo[idx][numAbsence][0]%=MOD;
                    }

                    // adding L
                    if (consecutiveLate>0) {
                        memo[idx][numAbsence][consecutiveLate]+=memo[idx-1][numAbsence][consecutiveLate-1];
                        memo[idx][numAbsence][consecutiveLate]%=MOD;
                    }
                }
            }
        }

        for (int numAbsence=0; numAbsence<2; numAbsence++) {
            for (int consecutiveLate=0; consecutiveLate<3; consecutiveLate++) {
                res+=memo[n][numAbsence][consecutiveLate];
                res%=MOD
            }
        }

        return res;
    }
};