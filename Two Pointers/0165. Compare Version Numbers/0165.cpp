#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int compareVersion(string version1, string version2) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int i=0;
        int j=0;
        int n=version1.size();
        int m=version2.size();
        int num1=0;
        int num2=0;
        while(i<n || j<m){
            num1=0;
            num2=0;
            while(i<n && version1[i]!='.'){
                num1=num1*10+(version1[i]-'0');
                i++;
            }
            i++;
            while(j<m && version2[j]!='.'){
                num2=num2*10+(version2[j]-'0');
                j++;
            }
            j++;
            if(num1<num2){
                return -1;
            }else if(num1>num2){
                return 1;
            }
        }
        while(i<n){
            num1=0;
            while(i<n && version1[i]!='.'){
                num1=num1*10+(version1[i]-'0');
            }
            if(num1) return 1;
        }
        while(j<m){
            num2=0;
            while(j<m && version2[j]!='.'){
                num2=num2*10+(version2[j]-'0');
            }
            if(num2) return -1;
        }
        return 0;
    }
};