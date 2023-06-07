class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (size_t i = 0; i < nums.size(); ++i) {
            pq.push(nums[i]);
        }
        while (pq.size() > k) {
            pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(val);
        while (pq.size() > k) {
            pq.pop();
        }
        return pq.top();
    }

    private:
        // by default, a priority queue in c++ will be a max heap.
        // priority_queue<int, vector<int>, greater<int> pq; --> minheap syntax
        priority_queue<int, vector<int>, greater<int>> pq;
        int k;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */