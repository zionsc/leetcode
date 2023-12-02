class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = defaultdict(int)
        remainder_count[0] = 1

        total = 0
        res = 0

        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder < 0:
                remainder += k
            
            res += remainder_count[remainder]
            remainder_count[remainder] += 1

        return res

