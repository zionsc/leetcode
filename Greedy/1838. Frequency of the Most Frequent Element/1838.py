class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        max_freq = 0
        sum = 0

        for r in range(len(nums)):
            sum += nums[r]

            # Adjust the window size based on the total increments allowed (k)
            while nums[r] * (r - l + 1) - sum > k: # total sum of all the values in the array --> in order to make everything nums[r] (nums[r] * len --> what if every number was nums[r]? then subtract sum --> difference between current values in the window to if they were all nums[r].. how much do we need to make everything nums[r] basically!!)
                sum -= nums[l]
                l += 1

            max_freq = max(max_freq, r - l + 1)

        return max_freq
