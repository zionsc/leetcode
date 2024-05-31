class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 0
        for num in nums:
            prefix ^= num
        
        diff_bit = 1 # 00001
        while not (diff_bit & prefix):
            diff_bit <<= 1
        
        a = b = 0

        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num
        
        return [a, b]