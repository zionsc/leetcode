#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        unordered_map<int, int> countMap;
        vector<int> remaining, result;

        for (int i = 0; i < arr2.size(); i++) {
            countMap[arr2[i]] = 0;
        }

        for (int i = 0; i < arr1.size(); i++) {
            if (countMap.find(arr1[i]) != countMap.end()) {
                countMap[arr1[i]]++;
            } else {
                remaining.push_back(arr1[i]);
            }
        }

        sort(remaining.begin(), remaining.end());

        for (int i = 0; i < arr2.size(); i++) {
            for (int j = 0; j < countMap[arr2[i]]; j++) {
                result.push_back(arr2[i]);
            }
        }

        for (int i = 0; i < remaining.size(); i++) {
            result.push_back(remaining[i]);
        }

        return result;
    }
};