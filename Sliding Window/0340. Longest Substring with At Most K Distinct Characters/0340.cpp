class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);


        unordered_map<char,int> freq;
        int res=0;
        int distinct=0;
        int l=0;
        
        for(int r=0; r<s.size(); ++r){
            freq[s[r]]++;
            if (freq[s[r]]==1){
                distinct++;
            }
            while(distinct>k){
                freq[s[l]]--;
                if (freq[s[l]]==0){
                    distinct--;
                }
                l++;
            }
            if(distinct<=k){
                res=max(res,r-l+1);
            }
        }
        return res;

    }
};