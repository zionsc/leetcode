class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n 
        max_size, max_index = 1, 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], 1 + dp[j])
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i
        
        res = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                res.append(nums[i])
                num = nums[i]
                max_size -= 1

        return res
