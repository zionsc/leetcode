class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = res = 0

        for num in nums:
            curr_sum += num
            res += prefix_sum[curr_sum - goal]
            prefix_sum[curr_sum] += 1
        
        return res