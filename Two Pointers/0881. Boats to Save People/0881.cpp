#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int res=0;
        int l=0;
        int r=people.size()-1;
        sort(people.begin(),people.end());

        while(l<=r){
            if(people[l]+people[r]<=limit){
                l++;
                r--;
            }else{
                r--;
            }
            res++;
        }
        return res;

    }
};