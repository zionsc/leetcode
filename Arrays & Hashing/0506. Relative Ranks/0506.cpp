#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    inline vector<string> findRelativeRanks(vector<int>& score) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        unordered_map<int,int>idxMap;
        int n=score.size();
        for(int i=0; i<n; ++i){
            idxMap[score[i]]=i;
        }
        vector<int>sortedArray(score.begin(),score.end());
        sort(sortedArray.begin(),sortedArray.end(),greater<int>());

        vector<string>res(n);
        for(int i=0; i<n; ++i){
            if(i==0){
                res[idxMap[sortedArray[i]]]="Gold Medal";
            } else if (i==1){
                res[idxMap[sortedArray[i]]]="Silver Medal";
            } else if (i==2){
                res[idxMap[sortedArray[i]]]="Bronze Medal";
            } else{
                res[idxMap[sortedArray[i]]]=to_string(i+1);
            }
        }
        return res;
    }
};