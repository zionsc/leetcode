#pragma GCC optimize("O3","unroll-loops","Oz","omit-frame-pointer","inline-functions","fast-math","lto","march=native")
class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<int>res({0,1});
        int n=arr.size();
        double l=0;
        double r=1;
    
        while(true){
            double m=(l+r)/2;
            int count=0;
            res[0]=0;
            for(int i=0; i<n; ++i){
                int j=i+1;
                while(j<n && arr[i]>m*arr[j]){
                    j++;
                }
                if(j==n) break;
                count+=n-j;
                if(res[0]*arr[j]<arr[i]*res[1]){
                    res[0]=arr[i];
                    res[1]=arr[j];
                }
            }
            if(count>k) {r=m;}
            else if(count<k) {l=m;}
            else if(count==k){return res;}
        }
    }
};