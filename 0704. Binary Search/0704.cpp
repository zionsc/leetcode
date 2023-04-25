class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;

        return binarySearch(nums, left, right, target);
    }

private: 
    int binarySearch(vector<int>& nums, int left, int right, int target) {
        if (left > right) {
            return -1;
        }

        // To prevent overflow
        int mid = left + (right - left)/2;

        // Base Case    
        if (target == nums[mid]) {
            return mid;
        }

        // Case 1: target less than mid
        else if (target < nums[mid]) {
            return binarySearch(nums, left, mid - 1, target);
        }

        // Case 2: target greater than mid
        else {
            return binarySearch(nums, mid + 1, right, target);
        }
    }
};