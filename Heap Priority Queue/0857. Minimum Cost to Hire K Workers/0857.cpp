#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","omit-frame-pointer","march=native","lto","fast-math")
class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        double res=DBL_MAX;
        int totalQuality=0;
        priority_queue<int>maxQualityHeap;

        vector<pair<double,int>>wageQuality;
        for(int i=0; i<wage.size(); ++i){
            wageQuality.push_back({double(wage[i])/quality[i],quality[i]});
        } sort(wageQuality.begin(),wageQuality.end());

        for(int i=0; i<wageQuality.size(); ++i){
            if(maxQualityHeap.size()==k){
                totalQuality-=maxQualityHeap.top();
                maxQualityHeap.pop();
            }
            totalQuality+=wageQuality[i].second;
            maxQualityHeap.push(wageQuality[i].second);
            if(maxQualityHeap.size()==k){
                res=min(res,totalQuality*wageQuality[i].first);
            }
        }
        return res;
    }
};
