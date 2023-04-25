class Solution {
public:
    vector<int> replaceElements(vector<int>& arr)
    {
        int n = arr.size();
        vector<int> v(n);
        v[n-1] = -1;
        for(int i = n - 2; i >= 0; --i) // second to last item
        {
            v[i] = max(v[i + 1], arr[i + 1]);
        }
        return v;
    }
};