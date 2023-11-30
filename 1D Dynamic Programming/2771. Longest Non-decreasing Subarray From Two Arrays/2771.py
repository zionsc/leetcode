class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 1:
            return 1

        dp = [[1, 1] for _ in range(len(nums1))]
        max_len = 0

        for i in range(1, len(nums1)):
            if nums1[i] >= nums1[i - 1]:
                dp[i][0] = 1 + dp[i - 1][0]
            else:
                dp[i][0] = 1
            if nums1[i] >= nums2[i - 1]:
                dp[i][0] = max(dp[i][0], 1 + dp[i - 1][1])

            """""" 

            if nums2[i] >= nums1[i - 1]:
                dp[i][1] = 1 + dp[i - 1][0]
            else:
                dp[i][1] = 1
            if nums2[i] >= nums2[i - 1]:
                dp[i][1] = max(dp[i][1], 1 + dp[i - 1][1])

            max_len = max(max_len, dp[i][0], dp[i][1])

        return max_len