class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        res = 0
        for num in nums:
            if num % 2 == 0:
                res += 1
            if res >= 2:
                return True
        return False