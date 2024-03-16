class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {0:-1}
        prefix = 0
        res = 0

        for i,v in enumerate(nums):
            prefix += 1 if v == 1 else -1
            if prefix not in prefix_sum:
                prefix_sum[prefix] = i
            else:
                res = max(res, i - prefix_sum[prefix])

        return res
            