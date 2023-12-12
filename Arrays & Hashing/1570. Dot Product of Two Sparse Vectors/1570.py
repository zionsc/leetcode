class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for n1, n2 in zip(self.sparse, vec.sparse):
            res += n1 * n2
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)