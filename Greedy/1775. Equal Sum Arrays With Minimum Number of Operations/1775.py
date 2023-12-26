class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
            return -1
        
        sum1,sum2 = sum(nums1), sum(nums2)

        if sum1 > sum2:
            return self.minOperations(nums2, nums1)

        nums1.sort()
        nums2.sort()

        res = 0
        i,j = 0, len(nums2) - 1
        while sum2 > sum1:
            if j < 0 or (i < len(nums1) and 6 - nums1[i] > nums2[j] - 1):
                sum1 += 6 - nums1[i]
                i += 1
            else:
                sum2 -= nums2[j] - 1
                j -= 1
            res += 1
        return res