class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        for i in range(min(k, len(nums1))): # all combinations of nums1[i] : nums2[0] FOR NOW --> add other combinations later
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0)) # the comparator is the sum --> so we get the min sum possible always

        while min_heap and k < len(res):
            curr_sum, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
