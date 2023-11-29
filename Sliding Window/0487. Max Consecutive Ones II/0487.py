class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_zero = last_zero = l = max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
                if num_zero == 2:
                    max_len = max(max_len, r - l)
                    num_zero = 1
                    l = last_zero + 1
                last_zero = r
            max_len = max(max_len, r - l + 1)
        return max_len