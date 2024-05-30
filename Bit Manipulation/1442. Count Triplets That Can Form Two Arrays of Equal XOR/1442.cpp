#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int countTriplets(vector<int>& arr) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int res = 0;
        for (int i=0; i<arr.size()-1; i++) {
            int a = 0;
            for (int j=i+1; j<arr.size(); j++) {
                a^=arr[j-1];
                int b=0;
                for (int k=j; k<arr.size(); k++) {
                    b^=arr[k];
                    if (a==b) res++;
                }
            }
        }

        return res;
    }
};