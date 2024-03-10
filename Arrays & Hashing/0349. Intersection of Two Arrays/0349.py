class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        visit = set()
        for num in nums1:
            visit.add(num)
        for num in nums2:
            if num in visit:
                res.append(num)
                visit.remove(num)
        return res