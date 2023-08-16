class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom-up DP approach: reason for that is because we want to check each possible subsequence
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)): # checking each subsequence i + 1 -> end

